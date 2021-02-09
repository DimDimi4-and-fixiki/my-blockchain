import datetime
import hashlib

#  Block Class Description


class Block(object):
    def __init__(self, transactions: list,
                 previous_hash: str, block_id: int):
        """
        transactions: list of Transactions
        previous_hash: Hash of a previous block
        """
        self.block_id = block_id
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = str(datetime.datetime.now())
        self.block_hash = self.encode_block()

    def encode_block(self) -> str:
        transactions_str = ""
        for transaction in self.transactions:
            user1 = transaction.sender
            user2 = transaction.recipient
            transactions_str += user1.username + " to " + user2.username + " " + str(transaction.value) + "\n"

        print(transactions_str)
        str_to_encode = transactions_str + self.previous_hash
        return hashlib.sha256(str_to_encode.encode()).hexdigest()

    def get_hash(self):
        return self.block_hash




