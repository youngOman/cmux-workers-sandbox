import subprocess
import sys
import unittest
from pathlib import Path

CLI = Path(__file__).with_name("cli.py")


def run(*args):
    return subprocess.run(
        [sys.executable, str(CLI), *args], capture_output=True, text=True
    )


class CliTest(unittest.TestCase):
    def assertUsageError(self, result):
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertNotEqual(result.stderr, "")

    def test_mean(self):
        r = run("mean", "1", "2", "3", "4")
        self.assertEqual(r.returncode, 0)
        self.assertEqual(r.stdout.strip(), "2.5")

    def test_median(self):
        r = run("median", "3", "1", "2")
        self.assertEqual(r.returncode, 0)
        self.assertEqual(r.stdout.strip(), "2")

    def test_median_float(self):
        r = run("median", "1.5", "2.5")
        self.assertEqual(r.returncode, 0)
        self.assertEqual(r.stdout.strip(), "2.0")

    def test_slug(self):
        r = run("slug", "Hello World")
        self.assertEqual(r.returncode, 0)
        self.assertEqual(r.stdout.strip(), "hello-world")

    def test_no_command(self):
        self.assertUsageError(run())

    def test_unknown_command(self):
        self.assertUsageError(run("sum", "1", "2"))

    def test_mean_empty(self):
        self.assertUsageError(run("mean"))

    def test_median_empty(self):
        self.assertUsageError(run("median"))

    def test_mean_not_number(self):
        self.assertUsageError(run("mean", "1", "abc"))

    def test_median_not_number(self):
        self.assertUsageError(run("median", "x"))

    def test_slug_missing_text(self):
        self.assertUsageError(run("slug"))


if __name__ == "__main__":
    unittest.main()
