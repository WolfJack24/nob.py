from ctypes import WinDLL, c_void_p, c_uint64, c_ulong

ker32 = WinDLL("kernel32.dll")

LPVOID = c_void_p
ULONG_PTR = c_uint64
SIZE_T = ULONG_PTR
DWORD = c_ulong

ker32.VirtualAlloc.argtypes = [
    LPVOID,  # lpAddress
    SIZE_T,  # dwSize
    DWORD,   # flAllocationType
    DWORD    # flProtect
]
ker32.VirtualAlloc.restype = LPVOID


def VirtualAlloc(
    lpAddress: LPVOID,
    dwSize: SIZE_T,
    flAllocationType: DWORD,
    flProtect: DWORD
) -> LPVOID:
    return ker32.VirtualAlloc(lpAddress, dwSize, flAllocationType, flProtect)
