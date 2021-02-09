from block import Block
from transaction import Transaction
from user import User


if __name__ == '__main__':

    # List of our Users:
    users = [User(1, "Dima", 10), User(2, "David", 2.4), User(3, "Mary", 4.3)]

    # List of our transactions:
    transactions = [Transaction(sender=users[-1], recipient=users[1], value=1),
                    Transaction(sender=users[0], recipient=users[1], value=3),
                    Transaction(sender=users[1], recipient=users[0], value=2),
                    Transaction(sender=users[0], recipient=users[-1], value=4)]

    # Blocks:
    block1 = Block(transactions=transactions[:2], previous_hash="Start Hash", block_id=1)
    block2 = Block(transactions=[transactions[2]], previous_hash=block1.get_hash(), block_id=2)
    block3 = Block(transactions=[transactions[-1]], previous_hash=block2.get_hash(), block_id=3)

    # List of blocks:
    blockchain = [block1, block2, block3]
    
    for i, block in enumerate(blockchain):
        print("Block_id:", i + 1, "Hash =", block.get_hash())



