import unittest
from stringcmp import do_stringcmp


class TestingStringComparisons(unittest.TestCase):
    def test_something(self):
        str1 = "specific"
        str2 = "pacific"
        cmp_methods = ["sgramshort", "editex", "syllaldistshort"]
        for method in cmp_methods:
            self.assertIsNotNone(do_stringcmp(cmp_method=method, str1=str1, str2=str2), method + " returned None")


if __name__ == '__main__':
    unittest.main()
