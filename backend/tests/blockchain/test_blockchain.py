from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA

def test_blockchain_instance():
    blockchain = Blockchain()

    assert isinstance(blockchain, Blockchain), "Blockchain instance is not created correctly"
    assert blockchain.chain[0].hash == GENESIS_DATA['hash'], "Genesis block hash does not match expected value"

def test_add_block():
    blockchain = Blockchain()
    data = "Test Block Data"
    
    blockchain.add_block(data)
    
    assert len(blockchain.chain) == 2, "Block was not added to the chain"
    assert blockchain.chain[-1].data == data, "Data in the new block does not match expected value"
    assert blockchain.chain[-1].last_hash == blockchain.chain[-2].hash, "Last hash of the new block does not match the previous block's hash"