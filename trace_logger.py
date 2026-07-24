class TraceLogger:

    def __init__(self):
        self.logs = []

    def log(self, message):

        print(message)
        self.logs.append(message)

    def save(self, filename):

        with open(filename, "w") as f:

            for line in self.logs:
                f.write(line + "\n")