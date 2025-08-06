# RolloutX

**RolloutX** is a Python package for designing fixed-sample and sequential A/B tests under rollout constraints. It provides theoretical guarantees for controlling Type I and Type II error, and includes both fast analytical solutions and visualization tools.

---

## 📦 Features

- ✅ Fixed-sample test design: compute β given (r, d), or solve for d or r
- ✅ Sequential test design: repeated significance test with error control
- ✅ Fast, simulation-free approximations
- ✅ Plotting support to visualize β vs rollout rate or days
- ✅ Full test coverage and modular design

---

## 🧪 Example Usage

```python
from rolloutx.fixed_sample.core import design_fixed_sample
from rolloutx.sequential.core import design_sequential

# Fixed-sample design: compute beta given r and d
res1 = design_fixed_sample(N=1000, p0=0.1, p1=0.13, alpha=0.05, r=0.5, d=10)

# Sequential design: solve for r given target beta
res2 = design_sequential(K=10, N=1000, p0=0.1, p1=0.13, alpha=0.05, beta=0.2)
