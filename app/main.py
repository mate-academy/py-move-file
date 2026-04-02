import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3:
        command_name, file_name, destination_path = command

        if "/" in destination_path:
            destination_path = destination_path.split("/")
            new_file_name = destination_path[-1]
            destination_path = destination_path[:-1]

            path = os.path.join(destination_path, new_file_name)
            os.makedirs(path, exist_ok=True)

        with (
            open(f"{file_name}", "r") as file_in,
            open(f"{destination_path}", "w") as file_out
        ):
            file_out.write(file_in.read())
            os.remove(file_name)
