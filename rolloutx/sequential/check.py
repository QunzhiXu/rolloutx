# ROLLOUTX/sequential/check.py

def _check_common(K, N, p0, p1, alpha):
    if not isinstance(K, int) or K <= 0:
        raise ValueError(f"K must be a positive integer. Got: {K}")
    
    if not isinstance(N, int) or N <= 0:
        raise ValueError(f"N must be a positive integer. Got: {N}")

    for key, val in [('p0', p0), ('p1', p1), ('alpha', alpha)]:
        if not (0 < val < 1):
            raise ValueError(f"{key} must be in (0, 1). Got: {val}")

    if p1 <= p0:
        raise ValueError(f"p1 must be strictly greater than p0. Got p0={p0}, p1={p1}")

    for key, val in [('p0', p0), ('p1', p1)]:
        if val * (1 - val) < 1e-6:
            raise ValueError(f"{key}*(1 - {key}) is too small and may cause numerical instability.")


def check_for_beta(K, N, p0, p1, alpha, r):
    """
    Check input parameters when rollout rate r is given and we want to compute beta.
    """
    _check_common(K, N, p0, p1, alpha)

    if not (0 < r <= 1):
        raise ValueError(f"Rollout rate r must be in (0, 1]. Got: {r}")


def check_for_r(K, N, p0, p1, alpha, beta):
    """
    Check input parameters when beta is given and we want to solve for r.
    """
    _check_common(K, N, p0, p1, alpha)

    if not (0 < beta < 1):
        raise ValueError(f"Target beta must be in (0, 1). Got: {beta}")
