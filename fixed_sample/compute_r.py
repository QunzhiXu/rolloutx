from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np


def compute_r(d, beta_target, alpha, p0, p1, N, r_grid=None):
    """
    Return the smallest r such that beta <= beta_target.
    """
    if r_grid is None:
        r_grid = np.linspace(0.01, 0.99, 500)

    for r in r_grid:
        beta_val, _ = _compute_beta_given_rd(r, d, alpha, p0, p1, N)
        if beta_val <= beta_target:
            c = _compute_c(alpha, p0, N, d)
            return r, c
    return None, None


def plot_beta_vs_r(d, alpha, p0, p1, N, r_grid=None):
    """
    Plot beta as a function of r.
    """
    if r_grid is None:
        r_grid = np.linspace(0.01, 0.99, 200)

    betas = []

    for r in r_grid:
        beta_val, _ = _compute_beta_given_rd(r, d, alpha, p0, p1, N)
        betas.append(beta_val)

    plt.figure(figsize=(8, 5))
    plt.plot(r_grid, betas, marker='o')
    plt.title("Type II Error β vs. Rollout Percentage r")
    plt.xlabel("Rollout Percentage (r)")
    plt.ylabel("Type II Error (β)")
    plt.grid(True)
    plt.show()


def _compute_beta_given_rd(r, d, alpha, p0, p1, N):
    std0 = (2 * N * d * p0 * (1 - p0)) ** 0.5
    z_alpha = norm.ppf(1 - alpha)
    c = z_alpha * std0
    num = c - r * N * d * (p1 - p0)
    den = (r * N * d * p1 * (1 - p1) + (2 - r) * N * d * p0 * (1 - p0)) ** 0.5
    beta = norm.cdf(num / den)
    return beta, c


def _compute_c(alpha, p0, N, d):
    std0 = (2 * N * d * p0 * (1 - p0)) ** 0.5
    return norm.ppf(1 - alpha) * std0
