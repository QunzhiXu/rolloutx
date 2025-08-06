def check_params(params):
    """
    Validates the input parameters for the fixed-sample design functions.

    Parameters:
        params (dict): dictionary of parameters. Possible keys include:
            - 'N': int > 0
            - 'alpha': float in (0, 1)
            - 'beta': float in (0, 1)
            - 'r': float in (0, 1)
            - 'd': int > 0
            - 'p0': float in (0, 1)
            - 'p1': float in (0, 1), and should be > p0

    Raises:
        ValueError: if any parameter is invalid
    """

    if 'N' in params:
        N = params['N']
        if not isinstance(N, int) or N <= 0:
            raise ValueError(f"N must be a positive integer. Got: {N}")

    for key in ['alpha', 'beta', 'r', 'p0', 'p1']:
        if key in params:
            value = params[key]
            if not (0 < value < 1):
                raise ValueError(f"{key} must be in (0, 1). Got: {value}")

    if 'd' in params:
        d = params['d']
        if not isinstance(d, int) or d <= 0:
            raise ValueError(f"d must be a positive integer. Got: {d}")

    if 'p0' in params and 'p1' in params:
        if params['p1'] <= params['p0']:
            raise ValueError(f"p1 must be greater than p0. Got: p0={params['p0']}, p1={params['p1']}")
