import unittest
import tests_12_1
import tests_12_2

test_test = unittest.TestSuite()
test_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
test_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_test)
