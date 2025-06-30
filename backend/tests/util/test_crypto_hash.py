from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    """
    Test the crypto_hash function with different inputs.
    """
    # Test with different order of arguments
    assert crypto_hash('one', 2, [3]) == crypto_hash([3], 2, 'one')
    
    # Test with different types of arguments
    assert crypto_hash('one', 2, [3]) != crypto_hash('two', 2, [3])
    
    # Test with empty input
    assert crypto_hash() == crypto_hash('')
    
    # Test with same input but different order
    assert crypto_hash(1, 2, 3) == crypto_hash(3, 2, 1)