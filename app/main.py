import os


def move_file(command: str) -> None:
    cmd = command.split()
    input_command, source_file, destination_file_path = cmd
    if input_command == "mv" and len(cmd) == 3:
        new_file_path = os.path.split(destination_file_path)
        if new_file_path[0]:
            os.makedirs(new_file_path[0], exist_ok=True)
            new_file = os.path.join(*new_file_path)
        else:
            new_file = new_file_path[1]

        with open(source_file) as file_out, open(new_file, "w") as file_in:
            file_in.write(file_out.read())

        os.remove(source_file)
