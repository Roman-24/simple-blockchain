# Example usage:
from block import Block
from simple_blockchain import Blockchain

if __name__ == "__main__":
    # create a blockchain and print the initial state
    my_blockchain = Blockchain()
    print("Blockchain initialized with Genesis Block:")
    print("Block 0 - Hash:", my_blockchain.get_latest_block().hash)

    # add new blocks to the blockchain
    for i in range(1, 4):
        new_block_data = f"Block {i} Data"
        new_block = Block(None, None, None, new_block_data)
        my_blockchain.add_block(new_block)
        print(f"Block {i} added to the blockchain:")
        print(f"Block {i} - Hash:", new_block.hash)
