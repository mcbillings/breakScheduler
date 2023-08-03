import unittest
import breakScheduler

class TestTime(unittest.TestCase):
    def test_multi_digit_am(self):
        time = breakScheduler.toHP(11, 0)
        self.assertEqual(time, 1100)
    def test_multi_digit_pm(self):
        time = breakScheduler.toHP(11, 1)
        self.assertEqual(time, 2300)

if __name__ == '__main__':
    unittest.main()