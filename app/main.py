import os


def move_file(command: str) -> None:
    command_parts = command.split(" ")

    if len(command_parts) < 3 or command_parts[0] != "mv":
        return

    linux_command, source_file, destination_path = command_parts

    if destination_path.find("/") == -1 and source_file != destination_path:
        os.rename(source_file, destination_path)
        return

    if destination_path[-1] == "/":
        os.makedirs(destination_path[:-1], exist_ok=True)
        with open(source_file, "r") as source_f, open(
            f"{destination_path}{source_file}", "w"
        ) as destination_f:
            destination_f.write(source_f.read())
        os.remove(source_file)

    else:
        ind = destination_path.rfind("/")
        os.makedirs(destination_path[:ind], exist_ok=True)
        with open(source_file, "r") as source_f, open(
            destination_path, "w"
        ) as destination_f:
            destination_f.write(source_f.read())
        os.remove(source_file)
