import unittest
import test_image_generator
import test_logger
import test_db

def run_all_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(test_image_generator))
    suite.addTests(loader.loadTestsFromModule(test_logger))
    suite.addTests(loader.loadTestsFromModule(test_db))

    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)

if __name__ == '__main__':
    run_all_tests()