
import unittest

from src.resiliencelint import validate_workload


class TestValidateWorkload(unittest.TestCase):
    def test_valid_rto_and_rpo(self):
        workload = {
            "workload": {
                "recovery": {
                    "rto": "4h",
                    "rpo": "15m",
                }
            }
        }
        self.assertEqual(validate_workload(workload), [])

    def test_missing_rto(self):
        workload = {
            "workload": {
                "recovery": {
                    "rpo": "15m",
                }
            }
        }
        errors = validate_workload(workload)
        self.assertEqual(len(errors), 1)
        self.assertIn("RTO is missing", errors[0])

    def test_missing_rpo(self):
        workload = {
            "workload": {
                "recovery": {
                    "rto": "4h",
                }
            }
        }
        errors = validate_workload(workload)
        self.assertEqual(len(errors), 1)
        self.assertIn("RPO is missing", errors[0])

    def test_empty_rto(self):
        workload = {
            "workload": {
                "recovery": {
                    "rto": "",
                    "rpo": "15m",
                }
            }
        }
        errors = validate_workload(workload)
        self.assertEqual(len(errors), 1)
        self.assertIn("RTO is missing", errors[0])

    def test_whitespace_rpo(self):
        workload = {
            "workload": {
                "recovery": {
                    "rto": "4h",
                    "rpo": "   ",
                }
            }
        }
        errors = validate_workload(workload)
        self.assertEqual(len(errors), 1)
        self.assertIn("RPO is missing", errors[0])


if __name__ == "__main__":
    unittest.main()
