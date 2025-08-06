from scipy.stats import norm

def compute_beta(r, d, alpha, p0, p1, N):
    """
    Compute the Type-II error (beta) and threshold c 
    given rollout percentage r and duration d.

    Parameters:
        r (float): rollout percentage
        d (int): rollout duration (days)
        alpha (float): Type-I error rate
        p0 (float): baseline conversion rate
        p1 (float): post-rollout conversion rate
        N (int): number of users per day

    Returns:
        (beta, c): tuple of Type-II error and threshold
    """
    std0 = (2 * N * d * p0 * (1 - p0)) ** 0.5
    z_alpha = norm.ppf(1 - alpha)
    c = z_alpha * std0

    num = c - r * N * d * (p1 - p0)
    den = (r * N * d * p1 * (1 - p1) + (2 - r) * N * d * p0 * (1 - p0)) ** 0.5
    beta = norm.cdf(num / den)

    return beta, c
