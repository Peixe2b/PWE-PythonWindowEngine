from typing import Any

from PWE.src.internal.user_system import PlatformSupport 


class __SDLFunc(object):
    """
    Represents a function from SDL library.
    
    Args:
        func_name (str): Name of the function.
        arg_type (Any): Type of the function arguments.
        return_type (Any): Type of the function return value.
    """

    def __init__(self, func_name: str, arg_type: Any, return_type: Any):
        self.func_name = func_name
        self.arg_type = arg_type
        self.return_type = return_type


class SDL_DLL(object):
    """
    Represents an SDL library interface for a specific platform.

    Args:
        name_dll (str): The name of the SDL dynamic-link library (DLL) file.
        platform (Any): The platform on which the SDL library is being used.
    """

    def __init__(self, name_dll: str, platform: PlatformSupport):
        self.name_dll = name_dll
        self.platform = platform.value
    