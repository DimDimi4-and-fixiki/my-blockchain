from user import User


class Transaction(object):
    """
    Class of Transaction
    Between two Users
    """
    def __init__(self, sender: User, recipient: User, value: float):
        """
        sender: User who sends money
        recipient: User who receives money
        value: Sum of a transaction
        """

        #  Initialing values:
        self.sender = sender
        self.recipient = recipient
        self.value = value
