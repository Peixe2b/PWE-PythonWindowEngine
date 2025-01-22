from PWE import get_version

class TestPWEVersion:
    PWE_VERSION = (1, 0, 0)

    def test_get_version_without_pwe_function(self):
        major = 1
        minor = 0
        patch = 0
        pwe_version = (major, minor, patch)

        assert pwe_version == self.PWE_VERSION

    def test_get_version_with_pwe_function(self):
        my_pwe_version = get_version() # (1, 0, 0)
        assert my_pwe_version == self.PWE_VERSION
