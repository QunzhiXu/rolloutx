# ROLLOUTX/sequential/compute_beta.py

import numpy as np
from scipy.stats import norm

def compute_gamma(alpha, K, N, p0):
    """
    Compute gamma = sqrt(log(1/alpha) / (K * N * p0 * (1 - p0)))
    """
    return np.sqrt(np.log(1 / alpha) / (K * N * p0 * (1 - p0)))

def compute_M(gamma, N, p0):
    """
    Compute M = gamma * N * p0 * (1 - p0)
    """
    return gamma * N * p0 * (1 - p0)

def compute_beta_sequential(r, K, N, p0, p1, alpha):
    """
    Compute the Type II error (beta) for the sequential rollout test.

    Parameters:
        r (float): rollout rate (0 < r <= 1)
        K (int): number of days
        N (int): number of users per day
        p0 (float): baseline conversion rate
        p1 (float): alternative conversion rate
        alpha (float): Type I error rate

    Returns:
        beta (float): approximated Type II error
    """
    gamma = compute_gamma(alpha, K, N, p0)
    M = compute_M(gamma, N, p0)

    numerator = M * K + (1 / gamma) * np.log(1 / alpha) - r * N * K * (p1 - p0)
    denominator = np.sqrt(
        (2 - r) * N * K * p0 * (1 - p0) + r * N * K * p1 * (1 - p1)
    )

    z = numerator / denominator
    return norm.cdf(z)
