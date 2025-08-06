# ROLLOUTX/tests/test_sequential.py

import pytest
from rolloutx.sequential.core import design_sequential


def test_design_sequential_given_r():
    result = design_sequential(
        K=10, N=1000, p0=0.1, p1=0.13, alpha=0.05, r=0.5
    )
    assert result is not None
    assert 'r' in result and abs(result['r'] - 0.5) < 1e-6
    assert 'beta' in result and 0 < result['beta'] < 1

def test_design_sequential_given_beta():
    result = design_sequential(
        K=10, N=1000, p0=0.1, p1=0.13, alpha=0.05, beta=0.2
    )
    assert result is not None
    assert 'r' in result and 0 < result['r'] <= 1
    assert 'beta' in result and abs(result['beta'] - 0.2) < 1e-2

def test_invalid_r_and_beta():
    result = design_sequential(
        K=10, N=1000, p0=0.1, p1=0.13, alpha=0.05, r=0.5, beta=0.2
    )
    assert result is None

def test_invalid_beta_impossible():
    result = design_sequential(
        K=5, N=100, p0=0.1, p1=0.11, alpha=0.01, beta=1e-4, plot=False
    )
    assert result is None
