import os
import typing


class ReadAndDelete:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> typing.IO:
        self.file = open(self.filename, "r")
        print(type(self.file))
        return self.file

    def __exit__(self,
                 exc_type: Exception,
                 exc_val: Exception,
                 exc_tb: Exception) -> None:
        self.file.close()
        os.remove(self.filename)


def create_directories(path: str) -> str:
    directories = path.split("/")
    full_dir = ""
    for i in range(len(directories) - 1):
        full_dir += directories[i] + "/"
        if not os.path.exists(full_dir):
            os.mkdir(full_dir)
    full_dir += directories[-1]
    return full_dir


def move_file(command: str) -> None:
    file_to_move = command.split()[1]
    if not os.path.exists(file_to_move):
        print(f"File '{file_to_move}' does not exist")
        return

    full_path = create_directories(command.split()[2])

    with (ReadAndDelete(file_to_move) as f_read,
          open(full_path, "w") as f_write):
        content = f_read.read()
        f_write.write(content)
