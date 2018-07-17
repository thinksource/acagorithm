import unittest
from ACalgorithm import ACBuild

class AlgorithmTest(unittest.TestCase):

    def setUp(self):
        self.text = "ushers"
        self.param = ["he", "she", "his", "hers"]
        # self.ac = ACBuild(text, Pattens)

    def test_build(self):
        ac = ACBuild(self.text, self.param)
        ac.buildGotoTree()
        ac.addFailure()
        ac.acSearch()
        self.assertEqual(ac.result["he"], [3])
        self.assertEqual(ac.result["she"],[2])
        self.assertEqual(len(ac.result["his"]),0)
        self.assertEqual(ac.result["hers"],[3])
    
if __name__ == '__main__':
    unittest.main()