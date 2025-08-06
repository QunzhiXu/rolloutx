# ROLLOUTX/sequential/core.py

from .check import check_for_beta, check_for_r
from .compute_beta import compute_beta_sequential
from .compute_r import find_r_min_sequential
from .plot_beta import plot_beta_vs_r


def design_sequential(K, N, p0, p1, alpha, r=None, beta=None, plot=False):
    """
    User-facing wrapper for sequential rollout experiment design.

    Parameters:
        K (int): number of days
        N (int): users per day
        p0 (float): baseline conversion rate
        p1 (float): post-change conversion rate
        alpha (float): Type-I error rate
        r (float, optional): rollout rate (proportion of users observed per day)
        beta (float, optional): target Type-II error rate
        plot (bool, optional): plot beta(r) curve when relevant

    Returns:
        dict or None: dictionary with keys 'r' and 'beta' if successful, else None
    """

    # Validate mutual exclusivity
    if (r is None and beta is None) or (r is not None and beta is not None):
        print("[Input Error] Please specify exactly one of r or beta.")
        return None

    # Mode 1: given r, compute beta
    if r is not None:
        try:
            check_for_beta(K, N, p0, p1, alpha, r)
            beta_val = compute_beta_sequential(r, K, N, p0, p1, alpha)
            return {
                'r': r,
                'beta': beta_val
            }
        except ValueError as e:
            print(f"[Parameter Error] {e}")
            return None

    # Mode 2: given beta, compute r
    if beta is not None:
        try:
            check_for_r(K, N, p0, p1, alpha, beta)
            r_val = find_r_min_sequential(beta, K, N, p0, p1, alpha)
            return {
                'r': r_val,
                'beta': beta
            }
        except ValueError as e:
            print(f"[Design Error] {e}")
            if plot:
                plot_beta_vs_r(K, N, p0, p1, alpha, beta_target=beta)
            return None
