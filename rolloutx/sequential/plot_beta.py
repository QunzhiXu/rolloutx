# ROLLOUTX/sequential/plot_beta.py

import numpy as np
import matplotlib.pyplot as plt
from .compute_beta import compute_beta_sequential

def plot_beta_vs_r(K, N, p0, p1, alpha, r_min=None, beta_target=None, save_path=None):
    """
    Plot beta(r) for a range of rollout rates.

    Parameters:
        K (int): number of days
        N (int): users per day
        p0 (float): baseline conversion rate
        p1 (float): post-rollout conversion rate
        alpha (float): Type I error rate
        r_min (float or None): optional, plot vertical line at this r
        beta_target (float or None): optional, plot horizontal line at this beta
        save_path (str or None): if provided, save plot to this file
    """

    r_values = np.linspace(0.01, 1.0, 200)
    beta_values = [compute_beta_sequential(r, K, N, p0, p1, alpha) for r in r_values]

    plt.figure(figsize=(8, 5))
    plt.plot(r_values, beta_values, label=r'$\beta(r)$', color='blue')

    if beta_target is not None:
        plt.axhline(beta_target, color='red', linestyle='--', label=f'Target β = {beta_target:.2f}')
    if r_min is not None:
        plt.axvline(r_min, color='green', linestyle='--', label=f'Min r = {r_min:.3f}')

    plt.xlabel("Rollout Rate (r)")
    plt.ylabel("Type II Error (β)")
    plt.title("Type II Error vs Rollout Rate")
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    else:
        plt.show()
