import mindsdb_sdk


class Mindsdb:
    """Mindsdb class to interact with Mindsdb SDK"""

    def __init__(self, email: str, password: str, repo: str):
        """
        Authenicating Mindsdb SDK with email and password
        """
        self.email = email
        self.password = password
        self.repo = repo

        self.is_authenticated = False
        self.is_initialized = False

    def authenticate(self):
        """
        connect user to mindsdb cloud
        """
        try:
            mindsdb_sdk.connect(login=self.email, password=self.password)
            self.is_authenticated = True
        except Exception as e:
            print(f"Error while authenticating user: {e}")

    def initialize(self):
        """
        Initialize the Github repo for octo
        """
