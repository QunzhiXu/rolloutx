from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

def compute_d(r, beta_target, alpha, p0, p1, N, d_max=100):
    """
    Return the smallest d such that beta <= beta_target.
    """
    for d in range(1, d_max + 1):
        beta_val, _ = _compute_beta_given_rd(r, d, alpha, p0, p1, N)
        if beta_val <= beta_target:
            c = _compute_c(alpha, p0, N, d)
            return d, c
    return None, None


def plot_beta_vs_d(r, alpha, p0, p1, N, d_range=(1, 50)):
    """
    Plot beta as a function of d.
    """
    ds = np.arange(d_range[0], d_range[1] + 1)
    betas = []

    for d in ds:
        beta_val, _ = _compute_beta_given_rd(r, d, alpha, p0, p1, N)
        betas.append(beta_val)

    plt.figure(figsize=(8, 5))
    plt.plot(ds, betas, marker='o')
    plt.title("Type II Error β vs. Rollout Duration d")
    plt.xlabel("Rollout duration (d)")
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
