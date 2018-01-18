import ranking
import unittest


# TODO: テストスイートをそのうち追加する。 http://www.yoheim.net/blog.php?q=20160903
# TODO: mock する？でも微妙だよなあ、API取りに行くのは保証する範囲外では？はじけるものをはじけてればOK？


class RankingTest(unittest.TestCase):
    def test_daily_invalid_date(self):
        result = ranking.daily(year=2012, month=1, day=1)
        self.assertEqual(result, [])

    # @unittest.skip("ちょっとAPI制限されそうでコワイ1")
    def test_daily_valid_date(self):
        result = ranking.daily(year=2017, month=1, day=1)
        rank_num = len(result)
        self.assertGreater(rank_num, 0)
        self.assertLessEqual(rank_num, 300)

    def test_weekly_invalid_date(self):
        result = ranking.weekly(year=2012, month=1, day=1)
        self.assertEqual(result, [])

        result = ranking.weekly(year=2017, month=9, day=11)
        self.assertEqual(result, [])

    # @unittest.skip("ちょっとAPI制限されそうでコワイ2")
    def test_weekly_valid_date(self):
        result = ranking.weekly(year=2017, month=9, day=12)
        rank_num = len(result)
        self.assertGreater(rank_num, 0)
        self.assertLessEqual(rank_num, 300)

    def test_monthly_invalid_date(self):
        result = ranking.monthly(year=2012, month=1, day=1)
        self.assertEqual(result, [])

        result = ranking.monthly(year=2017, month=9, day=2)
        self.assertEqual(result, [])

    # @unittest.skip("ちょっとAPI制限されそうでコワイ3")
    def test_monthly_valid_date(self):
        result = ranking.monthly(year=2017, month=9, day=1)
        rank_num = len(result)
        self.assertGreater(rank_num, 0)
        self.assertLessEqual(rank_num, 300)

    def test_quarterly_invalid_date(self):
        result = ranking.quarterly(year=2012, month=1, day=1)
        self.assertEqual(result, [])

        result = ranking.quarterly(year=2017, month=9, day=2)
        self.assertEqual(result, [])

    # @unittest.skip("ちょっとAPI制限されそうでコワイ4")
    def test_quarterly_valid_date(self):
        result = ranking.quarterly(year=2017, month=4, day=1)
        rank_num = len(result)
        self.assertGreater(rank_num, 0)
        self.assertLessEqual(rank_num, 300)


if __name__ == "__main__":
    unittest.main()
