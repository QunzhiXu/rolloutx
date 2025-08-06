# ROLLOUTX/sequential/compute_r.py

from scipy.optimize import bisect
from .compute_beta import compute_beta_sequential

def find_r_min_sequential(beta_target, K, N, p0, p1, alpha, tol=1e-4):
    """
    Find the minimal rollout rate r such that the Type II error is ≤ beta_target.
    Raises ValueError if no valid r is found in (0, 1].
    """

    def objective(r):
        return compute_beta_sequential(r, K, N, p0, p1, alpha) - beta_target

    # Check that root exists in [ε, 1]
    if objective(1.0) > 0:
        raise ValueError("Target beta is too small — even r = 1 can't achieve it.")

    return bisect(objective, a=1e-6, b=1.0, xtol=tol)
