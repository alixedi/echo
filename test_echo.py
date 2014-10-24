import unittest
from echo import echo, FailingTooHard


class TestEcho(unittest.TestCase):

    def test_without_failing(self):
        @echo(5)
        def add():
            return 2 + 1
        self.assertEquals(add(), 3)

    def test_with_exception(self):
        @echo(2)
        def conct():
            return 2 + "two"
        try:
            conct()
        except FailingTooHard:
            error = True
        self.assertTrue(error)


if __name__ == "__main__":
    unittest.main()
