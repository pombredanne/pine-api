import unittest

from pine.lib import version


class TestVersion(unittest.TestCase):

    def test_version(self):
        self.assertEqual(version.version_info["version"], "v1")
