FIB_ANSWERS = [
    (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21),
    (9, 34), (10, 55), (11, 89), (12, 144)
]

import series

@pytest.mark.parameterize('n, ans', FIB_ANSWERS)
def test_fib(n, ans):
    assert(series.fibonacci(n) == ans)
