import datetime
#  Block Class Description


class Block(object):
    def __init__(self, transactions: list,
                 previous_hash: str, block_id: int):
        """

        :param transactions: list of Transactions
        :param previous_hash: Hash of a previous block
        """
        self.block_id = block_id
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = str(datetime.datetime.now())
