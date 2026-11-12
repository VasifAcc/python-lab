class DatabaseConnection:
    def __init__(self, hostname, port, user, password):
        self.hostname = hostname
        self.port = port
        self.user = user
        self.password = password

    def show_parameters(self):
        print("Hostname:", self.hostname)
        print("Port:", self.port)
        print("User:", self.user)
        print("Password:", "*" * len(self.password))


if __name__ == "__main__":
    db = DatabaseConnection("localhost", 5432, "admin", "secret123")
    db.show_parameters()