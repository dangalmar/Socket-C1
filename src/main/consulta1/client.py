import socket
class Client:
    """
    A simple TCP client that connects to a server.

    Args:
        host (str): The hostname or IP address of the server.
        port (int): The port number of the server.

    Attributes:
        client_socket (socket.socket): The socket object used for communication.

    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

    def connect(self):
        """
        Establishes a connection to the server.

        Raises:
            ConnectionError: If the connection cannot be established.

        """
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print(f"Connection established with server at {self.host}:{self.port}")
        # Here, you can handle communication logic with the server


