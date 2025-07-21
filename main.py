from nobpy.libs.kernel32 import VirtualAlloc

def main() -> None:
    # Example usage of VirtualAlloc
    address = VirtualAlloc(None, 4096, 0x1000, 0x04)
    if address:
        print(f"Memory allocated at address: {address}")
    else:
        print("Memory allocation failed.")


if __name__ == "__main__":
    main()
