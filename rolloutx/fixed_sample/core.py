from .compute_beta import compute_beta
from .compute_d import compute_d, plot_beta_vs_d
from .compute_r import compute_r, plot_beta_vs_r
from .check import check_params



def design_fixed_sample(N, p0, p1, alpha, r=None, d=None, beta=None, plot=False):
    """
    User-facing wrapper for fixed-sample rollout experiment design.
    
    Parameters:
        N (int): daily sample size
        p0 (float): baseline conversion rate
        p1 (float): post-change conversion rate
        alpha (float): type-I error rate
        r (float, optional): rollout percentage
        d (int, optional): rollout days
        beta (float, optional): type-II error rate
        plot (bool, optional): whether to plot beta vs d or beta vs r when relevant

    Returns:
        dict or None: parameter values including c (threshold), or None if design fails
    """
    params = {
        'N': N,
        'p0': p0,
        'p1': p1,
        'alpha': alpha
    }
    if r is not None:
        params['r'] = r
    if d is not None:
        params['d'] = d
    if beta is not None:
        params['beta'] = beta

    return _design_fixed_sample_dict(params, plot=plot)


def _design_fixed_sample_dict(params, plot=False):
    """
    Internal version that takes a dictionary of parameters.

    Returns:
        dict or None
    """
    try:
        check_params(params)
    except ValueError as e:
        print(f"[Parameter Error] {e}")
        return None

    r = params.get('r')
    d = params.get('d')
    beta = params.get('beta')

    if r is not None and d is not None:
        beta_val, c = compute_beta(r, d, params['alpha'], params['p0'], params['p1'], params['N'])
        return {
            'r': r,
            'd': d,
            'beta': beta_val,
            'c': c
        }

    elif r is not None and beta is not None:
        d_val, c = compute_d(r, beta, params['alpha'], params['p0'], params['p1'], params['N'])
        if d_val is None:
            print("[Design Error] Cannot find rollout day (d) to satisfy the required type-II error.")
            if plot:
                plot_beta_vs_d(r, params['alpha'], params['p0'], params['p1'], params['N'])
            return None
        return {
            'r': r,
            'd': d_val,
            'beta': beta,
            'c': c
        }

    elif d is not None and beta is not None:
        r_val, c = compute_r(d, beta, params['alpha'], params['p0'], params['p1'], params['N'])
        if r_val is None:
            print("[Design Error] Cannot find rollout percentage (r) to satisfy the required type-II error.")
            if plot:
                plot_beta_vs_r(d, params['alpha'], params['p0'], params['p1'], params['N'])
            return None
        return {
            'r': r_val,
            'd': d,
            'beta': beta,
            'c': c
        }

    else:
        print("[Input Error] Please provide exactly two of the following: r, d, beta.")
        return None
