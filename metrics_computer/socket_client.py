import socket


def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket initialized")
    s.bind(('0.0.0.0', 8080))
    print("socket bound")
    s.listen(1)
    print("listen initiated")
    connection, address = s.accept()
    print("call acceppted")
    return connection
