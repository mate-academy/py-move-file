import os


def move_file(command: str) -> None:
    command_list: list = command.split()
    if (
            len(command_list) == 3
            and command_list[0] == "mv"
            and os.path.isfile(command_list[1])
    ):
        if "/" not in command_list[2]:
            os.rename(command_list[1], command_list[2])
        else:
            destination_path = os.path.split(command_list[2])[0]
            if not os.path.exists(destination_path):
                os.makedirs(destination_path, exist_ok=True)
            with (
                open(command_list[1], "r") as source_file,
                open(command_list[2], "w") as destination_file
            ):
                source: str = source_file.read()
                destination_file.write(source)
            os.remove(command_list[1])
