from typing import Tuple
from dataclasses import dataclass

PWE_VERSION = (1, 0, 2)


@dataclass
class __PWE_Version: # Entity for versioning
    major: int = PWE_VERSION[0]
    minor: int = PWE_VERSION[1]
    patch: int = PWE_VERSION[2]


def get_version() -> Tuple[int, int, int]:
    """
    Gets a tuple containing the major, minor, and patch of PWE.

    Returns:
        tuple: A tuple representing the PWE version in the format (major, minor, patch).
    """

    my_pwe_version = __PWE_Version()
    return (
        my_pwe_version.major,
        my_pwe_version.minor,
        my_pwe_version.patch
    )
