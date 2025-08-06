# tests/test_fixed_sample.py

import pytest
from ..fixed_sample.core import design_fixed_sample



def test_design_fixed_sample_basic():
    r = 0.5
    d = 14
    alpha = 0.05
    p0 = 0.1
    p1 = 0.12
    N = 1000

    result = design_fixed_sample(N, p0, p1, alpha, r=r, d=d)
    assert isinstance(result, dict)
    assert 'beta' in result and 'c' in result
    assert isinstance(result['beta'], float)
    assert 0 < result['beta'] < 1
    assert result['c'] > 0
