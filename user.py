#  User Class Description

class User(object):
    """
    User Class
    Stores information about the user
    """
    def __init__(self, **kwargs):
        user_id = kwargs.get("user_id")
        username = kwargs.get("username", None)
        balance = kwargs.get("balance", 0)

