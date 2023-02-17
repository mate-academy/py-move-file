import os


def move_file(command: str) -> None:
    command, first_file, second_file = command.split()
    second_file_path = second_file[:second_file.rfind("/")]

    if command == "mv":
        if not os.path.exists(second_file_path):
            os.makedirs(second_file_path)

        with (open(first_file, "r") as file_content,
              open(second_file, "w") as file_out):
            file_out.write(file_content.read())

        os.remove(first_file)
