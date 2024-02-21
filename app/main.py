import os


def move_file(command: str) -> None:
    if len(command.split(" ")) != 3:
        raise ValueError("Please, input correct request")
    if len(command.split()) == 3 and command.split()[0] == "mv":
        mv, file1, file2 = command.split()
        if os.path.dirname(file2):
            os.makedirs(os.path.dirname(file2), exist_ok=True)
        os.rename(file1, file2)
    else:
        raise ValueError("Used request without 'mv' command")
