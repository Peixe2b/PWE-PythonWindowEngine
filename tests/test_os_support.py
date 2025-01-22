from platform import system

class TestSystemSupport:
    EXPECTED_RESULT = ("Linux", "Windows")

    def test_view_user_platform_with_system(self): # Using platform library
        user_system = system()
        assert user_system in self.EXPECTED_RESULT

    def test_view_user_platform_with_pwe(self):
        pass
