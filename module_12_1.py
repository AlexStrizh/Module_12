import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = runner.Runner("Walker")
        for i in range(10):
            walker.walk()
        #self.assertEqual(walker.distance, 50)
        self.assertEqual(walker.distance, 100)

    def test_run(self):
        runner_ = runner.Runner("Runner")
        for i in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    def test_challenge(self):
        walker = runner.Runner("Walker")
        runner_ = runner.Runner("Runner")
        for i in range(10):
            walker.walk()
            runner_.run()
        self.assertNotEqual(runner_.distance, walker.distance)

if __name__ == '__main__':
    unittest.main()


# 100 != 50
#
# Expected :50
# Actual   :100
# <Click to see difference>
#
# Traceback (most recent call last):
#   File "C:\Users\gasto\YandexDisk\Документы\Обучение\Python\PythonProject\Module_12\module_12_1.py", line 10, in test_walk
#     self.assertEqual(walker.distance, 100)
# AssertionError: 50 != 100