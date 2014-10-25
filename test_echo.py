import unittest
from pyecho import echo, FailingTooHard


def fails_n_times(n, exception_type=Exception):
    # remembers how many times it's called, fails n times, returns None after
    _called = 0
    def fail_func():
        nonlocal _called
        if _called >= n:
            return
        _called += 1
        raise exception_type()
    return fail_func


class TestEcho(unittest.TestCase):

    def test_without_failing(self):
        @echo(5)
        def add():
            return 2 + 1
        self.assertEqual(add(), 3)

    def test_with_exception(self):
        @echo(2)
        def conct():
            return 2 + "two"
        self.assertRaises(FailingTooHard, conct)

    def test_n_minus_one_tries(self):
        try:
            # function fails twice; try 3 times
            echo(3)(fails_n_times(2))()
        except FailingTooHard:
            # test fails if wrapped function doesn't succeed
            self.fail()

    def test_doesnt_try_too_many_times(self):
        wrapped = echo(2)(fails_n_times(2))
        self.assertRaises(FailingTooHard, wrapped)


if __name__ == "__main__":
    unittest.main()
