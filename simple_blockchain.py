import time

from block import Block


class Blockchain:

    # blockchain constructor
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    # func for creation of genesis block
    # call only once for start journey of your blockchain
    def create_genesis_block(self):
        # Create the first block in the blockchain (genesis block)
        return Block(0, time.time(), 0, "Genesis Block")

    # func to get last block from blockchain
    def get_latest_block(self):
        return self.chain[-1]

    # func to add new block to blockchain
    # and set necessary params of block to correct values
    def add_block(self, block_to_add):
        block_to_add.previous_block_hash = self.get_latest_block().hash
        block_to_add.timestamp = time.time()
        block_to_add.current_height = self.get_latest_block().current_height + 1
        block_to_add.hash = block_to_add.calculate_hash()
        self.chain.append(block_to_add)
