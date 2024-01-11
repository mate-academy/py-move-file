import os


def move_file(command: str) -> None:
    mv, file_in, file_out = command.split()
    if mv == "mv":
        if not os.path.dirname(file_out):
            os.replace(file_in, file_out)
        else:
            other_place = os.path.dirname(file_out)
            if not os.path.exists(other_place):
                os.makedirs(other_place, exist_ok=True)
            if not os.path.exists(file_out):
                os.replace(file_in, file_out)
