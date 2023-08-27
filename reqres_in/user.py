class User:
    def __init__(self, name: str, job: str):
        self.name = name
        self.job = job

    def get_data(self):
        return {'name': self.name, 'job': self.job}
