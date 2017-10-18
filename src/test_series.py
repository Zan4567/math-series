import pytest

FIB_ANSWERS = [
    (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21),
    (9, 34), (10, 55), (11, 89), (12, 144)
]

LUC_ANSWERS = [
    (0, 0), (1, 2), (2, 1), (3, 3), (4, 4), (5, 7), (6, 11), (7, 18), (8, 29),
    (9, 47), (10, 76), (11, 123), (12, 199)
]

@pytest.mark.parametrize('n, ans', FIB_ANSWERS)
def test_fib(n, ans):
    from series import fibonacci
    assert(fibonacci(n) == ans)

@pytest.mark.parametrize('n, ans', LUC_ANSWERS)
def test_luc(n, ans):
    from series import lucas
    assert(lucas(n) == ans)

@pytest.mark.parametrize('n, ans', FIB_ANSWERS)
def test_sum_series_fib(n, ans):
    from series import sum_series
    assert(sum_series(n) == ans)

@pytest.mark.parametrize('n, ans', LUC_ANSWERS)
def test_sum_series_luc(n, ans):
    from series import sum_series
    assert(sum_series(n, 2, 1) == ans)
