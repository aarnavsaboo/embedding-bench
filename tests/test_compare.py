import unittest

from embedding_bench.compare import paired
from embedding_bench.batching import batches


class Tests(unittest.TestCase):
    def test_batches(self):
        self.assertEqual(list(batches([1,2,3,4,5],2)),[[1,2],[3,4],[5]])

    def test_pair(self):
        rows=[
            {"model":"a","query_id":"q","metrics":{"ndcg":.2}},
            {"model":"b","query_id":"q","metrics":{"ndcg":.6}},
        ]
        out=paired(rows,"a","b")
        self.assertAlmostEqual(out["mean_delta_right_minus_left"],.4)


if __name__=="__main__":
    unittest.main()
