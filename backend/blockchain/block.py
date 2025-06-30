import time 

from backend.util.crypto_hash import crypto_hash

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_data',
    'data': [],
}

class Block:
    '''
    Block: a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    '''
    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        '''
        String representation of the block.
        :return: string representation of the block
        '''
        return (
            'Block('
            f'data={self.data}, '
            f'timestamp={self.timestamp}, '
            f'hash={self.hash}, '
            f'last_hash={self.last_hash}, '
            f'hash={self.hash})'
        )
    
    @staticmethod
    def mine_block(last_hash, data):
        '''
        Mine a block based on he given last_block and data.
        '''
        timestamp = time.time_ns()
        last_hash = last_hash
        hash = crypto_hash(timestamp, last_hash, data)

        return Block(timestamp, last_hash, hash, data)

    @staticmethod
    def gensis():
        '''
        Create the genesis block.
        :return: the genesis block
        '''
        # return Block(
        #     GENESIS_DATA['timestamp'],
        #     GENESIS_DATA['last_hash'],
        #     GENESIS_DATA['hash'],
        #     GENESIS_DATA['data']
        # )
        return Block(**GENESIS_DATA)

    
def main():
    genesis_block = Block.gensis()
    block = Block.mine_block(genesis_block.hash, 'bar')
    print(block)

if __name__ == '__main__':
    main()