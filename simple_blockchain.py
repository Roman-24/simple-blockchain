import hashlib
import time


class Block:
    def __init__(self, previous_hash, timestamp, current_height, data, nonce=0):
        self.previous_block_hash = previous_hash
        self.timestamp = timestamp
        self.current_height = current_height
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (
                str(self.previous_block_hash)
                + str(self.timestamp)
                + str(self.current_height)
                + str(self.data)
                + str(self.nonce)
        )
        return hashlib.sha256(block_string.encode("utf-8")).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Create the first block in the blockchain (genesis block)
        return Block(0, time.time(), 0, "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, block_to_add):
        block_to_add.previous_block_hash = self.get_latest_block().hash
        block_to_add.timestamp = time.time()
        block_to_add.current_height = self.get_latest_block().current_height + 1
        block_to_add.hash = block_to_add.calculate_hash()
        self.chain.append(block_to_add)


# Example usage:
if __name__ == "__main__":
    # Create a blockchain and print the initial state
    my_blockchain = Blockchain()
    print("Blockchain initialized with Genesis Block:")
    print("Block 0 - Hash:", my_blockchain.get_latest_block().hash)

    # Add new blocks to the blockchain
    for i in range(1, 4):
        new_block_data = f"Block {i} Data"
        new_block = Block(None, None, None, new_block_data)
        my_blockchain.add_block(new_block)
        print(f"Block {i} added to the blockchain:")
        print(f"Block {i} - Hash:", new_block.hash)
