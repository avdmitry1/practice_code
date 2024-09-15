class InvalidMailError(Exception):
    """Custom exception for invalid email formats."""

    def __init__(self, mail: str):
        """Initializes the exception with the invalid email."""
        super().__init__(mail)
        self.mail = mail


    def __str__(self) -> str:
        return f'Invalid email format {self.mail}.'
    

class User:
    """Represents a user with an email address."""

    def __init__(self, email: str):
        """Initializes the user with an email address."""
        self.email = email


    def get_emain(self):
        """Returns the user's email address if valid, otherwise raises an exception."""
        if '@' in self.email:
            return self.email
        
        raise InvalidMailError(self.email)
    

try:
    user1 = User('avdmitry@gmail.com')
    print(user1.get_emain())
except InvalidMailError as e:
    print(e)