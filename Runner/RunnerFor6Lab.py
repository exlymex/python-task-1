import unittest

from BLL.lab6.TestCalculatorCore import TestCalculatorCore


class RunnerLab6:
    def run_tests(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorCore)
        unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    RunnerLab6().run_tests()