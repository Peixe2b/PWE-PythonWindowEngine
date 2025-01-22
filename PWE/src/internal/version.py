from dataclasses import dataclass

@dataclass
class __PWE_Version: # Entity for get version
    major = 1
    minor = 0
    patch = 1


def get_version() -> tuple:
    my_pwe_version = __PWE_Version()
    return (
        my_pwe_version.major,
        my_pwe_version.minor,
        my_pwe_version.patch
    )
