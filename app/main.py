import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    first_command = command_list[0]
    if first_command == "mv" and len(command) >= 6:

        file_old = command_list[1]
        destination = command_list[2]

        if destination.endswith("/"):
            destination_path = destination
            new_file_name = os.path.basename(file_old)
            file_new = os.path.join(destination_path, new_file_name)
        else:
            destination_path = os.path.dirname(destination)
            file_new = destination

        if destination_path:
            os.makedirs(destination_path, exist_ok=True)

        with open(file_old, "r") as file_in, open(file_new, "w") as file_out:
            data_file = file_in.read()
            file_out.write(data_file)

        os.remove(file_old)
