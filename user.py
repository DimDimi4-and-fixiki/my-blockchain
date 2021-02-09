#  User Class Description

class User(object):
    """
    User Class
    Stores information about the user
    """
    def __init__(self, user_id: int, username: str, balance: float):
        """
        user_id: ID of a User
        username: Name of a User
        balance: Sum of money a User has
        """

        # Initializing values:
        self.user_id = user_id
        self.username = username
        self.balance = balance
