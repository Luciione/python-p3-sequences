import io
import sys
from sequences import print_fibonacci

class TestPrintFibonacci:
    def test_print_fibonacci_zero(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(0)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[]\n'

    def test_print_fibonacci_one(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(1)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[0]\n'  # Modify the assertion here

    def test_print_fibonacci_two(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(2)
        sys.stdout = sys.__stdout__
    
        assert captured_out.getvalue() == '0\n1\n'


    def test_print_fibonacci_ten(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(10)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n'
