import threading

from load_test import LoadTest
from server import Server

if __name__ == "__main__":
    HOST = "127.0.0.1"  # Change this to the server's IP address
    PORT = 12345  # Server listening port

    server = Server(HOST, PORT)

    # Start the server in a separate thread
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    # Simulate load with LoadTest
    load_test = LoadTest(HOST, PORT)
    message = "a"
    num_clients = 3

    # Start client simulation in a separate thread
    load_test_thread = threading.Thread(target=load_test.client_simulation, args=(message, num_clients))
    load_test_thread.start()

    # Wait for both threads to finish
    server_thread.join()
    load_test_thread.join()