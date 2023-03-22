# Required packages
import unittest
import nbconvert
import os
import pandas

# Assignment-specific packages
import numpy as np

# Convert the assignment Jupyter notebooks into something we can import
with open("test_assignment.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)


with open("test_assignment.py", "w") as f:
    f.write(python_file)

# Import the converted file. Best to import only the variables you want to test
from test_assignment import q1, q2, q3

# Here is where you will write your tests
class TestSolution(unittest.TestCase):
    # You can fill this out if you are testing functions/classes, or want private tests
    # The name must be setUp(self)

    def setUp(self):
        pass

    # All tests need to start with "test_..."
    def test_q1(self):
        # Numpy has an extensive test suite.
        # It's best to use allclose instead of equal to avoid problems with machine precision
        np.testing.assert_allclose(q1, 45.0)
        return


    def test_q2(self):
        # It also works if testing an array
        # You can write the solution yourself as follows. But students will be able to see your solution
        q2_soln = 4 * np.arange(10)
        np.testing.assert_allclose(q2, q2_soln)
        return


    def test_q3(self):
        # Instead, it's better to hardcode the solution if possible
        q3_soln = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 19])
        np.testing.assert_allclose(q3, q3_soln)
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
    score_df = pandas.DataFrame(
        {
            "Total Tests": total_tests,
            "Number of Test Failures": num_failures,
            "Number of Test Errors": num_errors,
            "Number of Skipped Tests": num_skipped,
            "Student Score": student_score,
        }, index=[0])

    # Write dataframe to csv
    score_df.to_csv("student_score.csv", index=False)





