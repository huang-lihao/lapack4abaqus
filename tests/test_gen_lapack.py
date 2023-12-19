import unittest


class TestGenerateLAPACK(unittest.TestCase):
    def test_gen_lapack(self):
        import os

        from lapack4abaqus import gen_lapack
        if not os.path.exists("temp"):
            os.mkdir("temp")
        os.chdir("temp")
        gen_lapack(["dgetrf", "dgetri"])

if __name__ == "__main__":
    unittest.main()