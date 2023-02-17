import os


def move_file(command: str) -> None:
    command, first_file, second_file = command.split()
    directories = os.path.split(second_file)[0]

    if command == "mv":
        if not os.path.exists(directories):
            os.makedirs(directories)

        with (open(first_file, "r") as file_content,
              open(second_file, "w") as file_out):
            file_out.write(file_content.read())

        os.remove(first_file)
