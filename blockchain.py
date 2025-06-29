from block import Block

class Blockchain:
    '''
    Blockchain: a public ledger of transactioons.
    Implemented as a list of blocks - data sets of transactions
    '''

    def __init__(self):
        self.chain = [Block.gensis()]

    def add_block(self, data):
        '''
        Add a block to the blockchain.
        :param data: data to be stored in the block
        '''
        self.chain.append(Block.mine_block(self.chain[-1].hash, data))

    def __repr__(self):
        '''
        String representation of the blockchain.
        :return: string representation of the blockchain
        '''
        return f'Blockchain:\n{self.chain}'

def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    blockchain.add_block('three')

    print(blockchain)

if __name__ == '__main__':
    main()