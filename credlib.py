class Credential:
    def __init__(self, hostname: str, username: str, password: str) -> None:
        self.hostname = hostname
        self.username = username
        self.password = password

    def get(self, *args):

        if len(args) == 1 and isinstance(args[0], Credential):
            hostname = args[0].hostname
            username = args[0].username
            password = args[0].password
        elif len(args) == 3:
            hostname = args[0]
            username = args[1]
            password = args[2]
        else:
            raise ValueError("Invalid arguments")

        return hostname, username, password
