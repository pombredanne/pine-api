import unittest

from pine import version

class TestVersion(unittest.TestCase):

    def test_version(self):
        info = version.version_info()

        self.assertEqual(info["version"], "v1")
        self.assertEqual(info["accept"], "application/vnd.pine.v1+json")
