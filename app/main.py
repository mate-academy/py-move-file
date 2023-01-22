import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_name, file_name, destination_path = command.split()

        if "/" in destination_path:
            destination_path = destination_path.split("/")
            new_file_name = destination_path[-1]
            destination_path = destination_path[:-1]
            for path in destination_path:
                os.makedirs(path)
                new_file_name = os.path.join(path, new_file_name)

        with (
            open(f"{file_name}", "r") as file_in,
            open(f"{destination_path}", "w") as file_out
        ):
            file_out.write(file_in.read())
            os.remove(file_name)
