# Pytest Decorators

I would like to share **Pytest Decorators** with you. I cannot list each decorator, but I'll explain them as best I can. Let's start with first one;

## pytest.mark.parametrize()

```Python
@pytest.mark.parametrize("a, b, expected_sum", [
    (2, 3, 5),
    (0, 0, 0),
    (-2, 5, 3),
])
def test_calculate_sum(a, b, expected_sum):
    assert calculate_sum(a, b) == expected_sum
```

That decorator allows you to define multiple input parameters and expected outputs for a single test function, reducing the amount of code you need to write for similar test cases.

## pytest.mark.skip()

```Python
@pytest.mark.skip(reason="Test temporarily excluded due to a known issue")
def test_skipped_function():
    assert True
```

In this example, @pytest.mark.skipif decorator is used to skip the test_skipped_function() if the current version of Python is less than 3.0. The reason for skipping the test is specified as an argument to the decorator.

## pytest.mark.xfail()

```Python
@pytest.mark.xfail(raises=ZeroDivisionError, reason="Test expected to raise a ZeroDivisionError")
def test_expected_exception():
    a = 1 / 0
```

When the test suite is executed, the test_function() will fail and the test_expected_exception() will raise a ZeroDivisionError, which is the expected exception. The test will be marked as an expected failure and reported as an XPASS.

## pytest.mark.usefixtures()

```Python
@pytest.fixture
def my_fixture():
    return "Hello, world!"

@pytest.mark.usefixtures("my_fixture")
def test_function():
    assert my_fixture == "Hello, world!"
```

In this example, the **my_fixture()** fixture function returns the string "Hello, world!". The **@pytest.mark.usefixtures** decorator is used to provide the my_fixture fixture function to the **test_function()**. The my_fixture fixture function can now be used inside the **test_function()**.

When the test suite is executed, the my_fixture fixture function is called before the **test_function()** is executed. The **test_function()** can access the fixture function using the same name as the fixture function. The **test_function()** then asserts that the value returned by the my_fixture() fixture function is equal to the string "Hello, world!".

You can also use **@pytest.mark.usefixtures** decorator with multiple fixture functions.

## pytest.mark.filterwarnings()

```Python
@pytest.mark.filterwarnings("ignore:invalid value encountered in log")
def test_function():
    import numpy as np
    x = np.array([-1, 0, 1])
    with np.errstate(invalid='ignore'):
        y = np.log(x)
    assert y.tolist() == [np.nan, -np.inf, 0.0]
```

In this example, the test_function() uses the numpy library to compute the natural logarithm of an array x that contains some negative values. Since the natural logarithm of a negative number is undefined, this would normally result in a RuntimeWarning being issued by numpy.

When the test suite is executed, the test_function() is executed, and the warning message is issued by numpy. However, since the test is marked as ignoring that specific warning, the warning is not reported as an error, and the test passes as expected.
