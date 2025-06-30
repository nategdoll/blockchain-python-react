from backend.blockchain.block import Block, GENESIS_DATA

def test_mine_block():
    """
    Test the mine_block method of the Block class.
    """
    last_block = Block.gensis()
    data = 'Test Data'
    block = Block.mine_block(last_block.hash, data)
    
    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == last_block.hash
    assert block.hash is not None
    assert block.timestamp is not None

def test_genesis():
    """
    Test the genesis method of the Block class.
    """
    genesis_block = Block.gensis()
    
    assert isinstance(genesis_block, Block)
    
    for key, value in GENESIS_DATA.items():
        assert getattr(genesis_block, key) == value, f"Genesis block {key} does not match expected value"