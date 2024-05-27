import os

BUFFER_SIZE = 256


def move_file(command: str) -> None:
    operators = command.split(" ")
    first_path, second_path = operators[1::]

    # create directory if needed
    directory_path = os.path.split(second_path)[0]
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    with (open(first_path, "r") as file_read,
          open(second_path, "w") as file_write):
        buffer = file_read.read(BUFFER_SIZE)
        while buffer:
            file_write.write(buffer)
            buffer = file_read.read(BUFFER_SIZE)

    os.remove(first_path)
