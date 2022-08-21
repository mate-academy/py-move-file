class CommandError(Exception):
    def __init__(self, command):
        self.command = command

    def __str__(self):
        return f'No such command: {self.command}'


class MoveFileExistsError(Exception):
    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return f'File {self.file_name} already exists'
