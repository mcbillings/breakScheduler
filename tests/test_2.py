import unittest
import breakScheduler

class TestTime(unittest.TestCase):
    def test_single_digit_am(self):
        time = breakScheduler.toHP(1, 0)
        self.assertEqual(time, 100)
    def test_single_digit_pm(self):
        time = breakScheduler.toHP(1, 1)
        self.assertEqual(time, 1300)


if __name__ == '__main__':
    unittest.main()