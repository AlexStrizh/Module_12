import unittest
import module_12_1
import module_12_2

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)