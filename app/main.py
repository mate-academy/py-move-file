import os


def move_file(command: str) -> None:

    if len(command.split()) == 3:
        command, source_file_path, destination_file_path = command.split()
        print(destination_file_path)
        if command == "mv" and os.path.split(destination_file_path)[0] != "":
            os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)
        with (open(source_file_path, "r") as file_on,
              open(destination_file_path, "w") as file_out):
            file_out.write(file_on.read())
        os.remove(source_file_path)
