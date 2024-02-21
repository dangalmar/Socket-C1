import socket
import threading

class Test:
    

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.completed_requests = 0
        self.successful_responses = 0
        self.lock = threading.Lock()
        self.event = threading.Event()

    def client_simulation(self, message, num_clients):
        
        for _ in range(num_clients):
            threading.Thread(target=self.connect_and_send, args=(message, num_clients)).start()

    def connect_and_send(self, message, num_clients):
        
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
       
        self.event.wait()
        print(f"Successful responses: {self.successful_responses}")
