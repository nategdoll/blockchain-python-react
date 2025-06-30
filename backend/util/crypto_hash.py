import hashlib
import json

def crypto_hash(*args) -> str:
    """
    Generate a SHA-256 hash of the given arguments.

    Returns:
        str: The SHA-256 hash of the input data.
    """
    joined_data = ''.join(sorted(map(str, args)))

    return hashlib.sha256(joined_data.encode()).hexdigest()
    
def main():
    print(f"crypto_hash('one', 2 , [3]): {crypto_hash('one', 2, [3])}")
    print(f"crypto_hash([3], 2 ,'one'): {crypto_hash([3], 2, 'one')}")

if __name__ == "__main__":
    main()

