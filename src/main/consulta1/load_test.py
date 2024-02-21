import socket
import threading

class LoadTest:
    """
    This class is used to simulate a load test on a server.

    Args:
        host (str): The hostname or IP address of the server.
        port (int): The port number of the server.

    Attributes:
        completed_requests (int): The number of requests that have been completed.
        successful_responses (int): The number of successful responses that have been received.
        lock (threading.Lock): A lock for thread synchronization.
        event (threading.Event): An event for signaling thread completion.
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.completed_requests = 0
        self.successful_responses = 0
        self.lock = threading.Lock()
        self.event = threading.Event()

    def client_simulation(self, message, num_clients):
        """
        Simulate multiple clients sending requests to the server.

        Args:
            message (str): The message to send to the server.
            num_clients (int): The number of clients to simulate.
        """
        for _ in range(num_clients):
            threading.Thread(target=self.connect_and_send, args=(message, num_clients)).start()

    def connect_and_send(self, message, num_clients):
        """
        Connect to the server and send a request.

        Args:
            message (str): The message to send to the server.
            num_clients (int): The number of clients that are sending requests.

        Raises:
            Exception: An exception that occurs when there is an error connecting or sending the request.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                s.sendall(message.encode())
                response = s.recv(1024)
                decoded_response = response.decode()
                print(f"Received response: {decoded_response}")
                if "positive" in decoded_response.lower():  # Puedes ajustar la lógica según la respuesta del servidor
                    with self.lock:
                        self.successful_responses += 1
        except Exception as e:
            print(f"Error: {e}")
        finally:
            with self.lock:
                self.completed_requests += 1
                if self.completed_requests >= num_clients:
                    self.event.set()
                    print(f"Completed requests: {self.completed_requests}")

    def wait_for_completion(self):
        """
        Wait for all clients to complete their requests and signal thread completion.
        """
        self.event.wait()
        print(f"Successful responses: {self.successful_responses}")
