from user import User


class Transaction(object):
    """
    Class of Transaction
    Between two Users
    """
    def __init__(self, sender: User, recipient: User, valuue: float):
        self.sender = sender
        self.recipient = recipient
        self.value = value
