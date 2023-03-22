# Required packages
import unittest
import nbconvert

# Assignment-specific packages
import numpy as np
import pandas as pd
import pyvista as pv
import matplotlib.pyplot as plt
# Convert the assignment Jupyter notebooks into something we can import


# Import the converted file. Best to import only the variables you want to test
from project1_2 import aperture_statistics, aperture_mean, roughness_coeff, tortuosity, perm

# Here is where you will write your tests
class TestSolution(unittest.TestCase):
    # You can fill this out if you are testing functions/classes, or want private tests
    # The name must be setUp(self)

    def setUp(self):
        np.random.seed(0)
        self.aperture = np.random.randint(0,150,size=(100,100))
        pass

    # All tests need to start with "test_..."
    def test_q1(self):
        # Numpy has an extensive test suite.
        # It's best to use allclose instead of equal to avoid problems with machine precision
        np.testing.assert_allclose(aperture_statistics(self.aperture), (0,149))
        return


    def test_q2(self):
        # It also works if testing an array
        # You can write the solution yourself as follows. But students will be able to see your solution
       
        np.testing.assert_allclose(aperture_mean(self.aperture), 74.5306)
        return
        
    def test_q3(self):
        # It also works if testing an array
        # You can write the solution yourself as follows. But students will be able to see your solution
       
        np.testing.assert_allclose(roughness_coeff(self.aperture), 61.319589039718785)
        return

        
    def test_q4(self):
        # Instead, it's better to hardcode the solution if possible
        np.testing.assert_allclose(tortuosity(self.aperture), 49.970110174196435)
        return
        
    def test_q5(self):
        np.testing.assert_allclose(perm(self.aperture), 462.90086136333343)
        return
        


    
        


if __name__ == "__main__":
    tester = unittest.main(verbosity=2, exit=False)

    # Count number of total tests
    total_tests = tester.result.testsRun

    # Number of failed, errors, and skipped tests
    num_failures = len(tester.result.failures)
    num_errors = len(tester.result.errors)
    num_skipped = len(tester.result.skipped)

    # Final student score
    student_score = total_tests - (num_failures + num_errors + num_skipped)
    print(f"Score: {student_score}/{total_tests}")

    # Write student score to Pandas dataframe
    score_df = pd.DataFrame(
        {
            "Total Tests": total_tests,
            "Number of Test Failures": num_failures,
            "Number of Test Errors": num_errors,
            "Number of Skipped Tests": num_skipped,
            "Student Score": student_score,
        }, index=[0])

    # Write dataframe to csv
    score_df.to_csv("student_score.csv", index=False)
