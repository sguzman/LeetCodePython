import unittest
from _6_zigzag_conversion import zigzag_conversion


class MyTestCase(unittest.TestCase):
    def general_test(self, s: str, num_rows: int, output: str) -> None:
        solution: zigzag_conversion.Solution = zigzag_conversion.Solution()
        actual: str = solution.convert(s, num_rows)

        self.assertEqual(output, actual)

    def test_1(self):
        self.general_test('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR')

    def test_2(self):
        self.general_test('PAYPALISHIRING', 4, 'PINALSIGYAHRPI')


if __name__ == '__main__':
    unittest.main()
