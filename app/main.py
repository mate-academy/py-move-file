import os


def move_file(command: str) -> None:
    if len(command) >= 3:
        mv, source, new_path = command.split()
        if mv == "mv":
            path = os.path.dirname(new_path)
            if path:
                os.makedirs(path, exist_ok=True)

            with open(source, "r") as file_output, open(new_path, "w") as file_input:
                file_input.write(file_output.read())

            os.remove(source)
