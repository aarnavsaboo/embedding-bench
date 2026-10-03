import unittest
from embedding_bench.ranking import rank
from embedding_bench.metrics import evaluate


class Tests(unittest.TestCase):
    def test_rank(self):
        docs = {"x": [1.0, 0.0], "y": [0.0, 1.0]}
        self.assertEqual(rank([1.0, 0.0], docs)[0], "x")

    def test_metrics(self):
        out = evaluate(["b", "a"], {"a"}, 2)
        self.assertEqual(out["mrr"], .5)


if __name__ == "__main__":
    unittest.main()
