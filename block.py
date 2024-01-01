import hashlib


class Block:

    # block constructor
    # to this example simple as is possible nonce is allways zero
    def __init__(self, previous_hash, timestamp, current_height, data, nonce=0):
        self.previous_block_hash = previous_hash
        self.timestamp = timestamp
        self.current_height = current_height
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    # func for calculate hash of block
    # hash func SHA256
    def calculate_hash(self):
        block_string = (
                str(self.previous_block_hash)
                + str(self.timestamp)
                + str(self.current_height)
                + str(self.data)
                + str(self.nonce)
        )
        return hashlib.sha256(block_string.encode("utf-8")).hexdigest()
