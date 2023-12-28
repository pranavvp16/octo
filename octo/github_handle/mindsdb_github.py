import mindsdb_sdk
import subprocess
import time

class Mindsdb_Github:
    """Mindsdb class to interact with Mindsdb SDK"""

    def __init__(self, repo: str, owner: str):
        """
        Authenicating Mindsdb SDK with email and password
        """
        self.repo = repo
        self.owner = owner
        self.connection_string = "http://127.0.0.1:47334"

        self.is_authenticated = False
        self.is_initialized = False

    def connect_local(self):
        """
        Connect to local installation of mindsdb
        """
        # TODO: Will need this print to moved in cli.py and displayed using rich
        print("Starting mindsdb local server")

        # Run shell command to start the local mindsdb server
        process = subprocess.Popen(['python', '-m', 'mindsdb'])
        while not self.is_authenticated:
            try:
                server = self._connect_local()
                self.is_authenticated = True
            except Exception:
                time.sleep(10)

        return server, process

    def authenticate(self, email: str, password: str):
        """
        connect user to mindsdb cloud
        """
        try:
            server = mindsdb_sdk.connect(login=email, password=password)
            self.is_authenticated = True
        except Exception as e:
            print(f"Error while authenticating user: {e}")


    def initialize(self):
        """
        Initialize the GitHub repo for octo
        """

    def _connect_local(self):
        """
        Connect to local installation of mindsdb
        """
        server = mindsdb_sdk.connect(self.connection_string)
        server.databases.list()         # If not connected this line would raise an exception
        return server
