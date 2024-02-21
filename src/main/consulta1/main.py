import threading

from test import Test
from server import Server

if __name__ == "__main__":
    HOST = "127.0.0.1"  # Change this to the server's IP address
    PORT = 12345  # Server listening port

    server = Server(HOST, PORT)

    # Start the server in a separate thread
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    # Simulate load with Test
    load_test = Test(HOST, PORT)
    message = "1"
    num_clients = 15000

    # Start client simulation in a separate thread
    load_test_thread = threading.Thread(target=load_test.client_simulation, args=(message, num_clients))
    load_test_thread.start()

    # Wait for both threads to finish
    server_thread.join()
    load_test_thread.join()