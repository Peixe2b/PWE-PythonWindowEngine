from ctypes import (
    Structure,
    c_uint8,
    byref
)
from typing import Tuple

class __SDL_Version(Structure): # SDL Version structure
    _fields_ = [
        ('major', c_uint8),
        ('minor', c_uint8),
        ('patch', c_uint8)
    ]


def get_sdl_version() -> Tuple[c_uint8, c_uint8, c_uint8]: # After return (int, int, int) 
    """
    Return the version of DLL SDL

    Returns:
        Tuple[c_uint8, c_uint8, c_uint8]: SDL version
    """

    sdl_version = __SDL_Version()
    return (
        sdl_version.major,
        sdl_version.minor,
        sdl_version.patch
    )

if __name__ == "__main__":
    print(get_sdl_version())
