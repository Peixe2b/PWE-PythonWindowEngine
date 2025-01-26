import PWE

class TestPWEVersion:

    def test_get_version_without_pwe_function(self):
        """Test the version of PWE with a tuple"""
        
        major = 1
        minor = 0
        patch = 2
        pwe_version = (major, minor, patch)
        assert pwe_version == PWE.PWE_VERSION

    def test_get_version_with_pwe_function(self):
        """Test the version of PWE with a pwe function"""

        my_pwe_version = PWE.get_version() # Get a tuple with PWE version
        assert my_pwe_version == PWE.PWE_VERSION
    
    def test_sdl_wrapper(self):
        """Test the SDL facade"""

        sdl_dll = PWE.SDL_DLL("libSDL2.so", PWE.PlatformSupport.LINUX)
        assert sdl_dll.name_dll == "libSDL2.so"
        assert sdl_dll.platform == "Linux"

    def test_sdl_version(self):
        """Test the version of SDL"""
        pass
