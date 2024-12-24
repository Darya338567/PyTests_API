
from adder.adder import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 3, 3) == 9

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 7, 2) == 5

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 4, 3) == 7

    def test_multiply_calculate_not_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 88

    def test_division_calculate_not_correctly(self):
        assert self.calc.division(self, 10, 2) == 6

    def test_adding_calculate_not_correctly(self):
        assert self.calc.adding(self, 8, 1) == 10

    def test_subtraction_calculate_not_correctly(self):
        assert self.calc.subtraction(self, 8, 2) == 36
