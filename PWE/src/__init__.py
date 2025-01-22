from PWE.src.internal.pwe_version import PWE_Version

def get_version() -> tuple: # return PWE version
    return (
        PWE_Version.major,
        PWE_Version.minor,
        PWE_Version.patch
    )
