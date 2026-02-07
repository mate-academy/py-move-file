import os


def move_file(command: str) -> None:
    command_in_list = command.split()
    if len(command_in_list) != 3:
        return
    linux_command, source_file, destination_file = command_in_list
    if linux_command != "mv":
        return
    if destination_file[-1] == os.sep:
        destination_file += source_file
    path = command_in_list[2].split("/")
    for element_of_path in range(len(path)):
        if element_of_path == len(path) - 1 and path[element_of_path]:
            try:
                with (open(source_file, "r") as file_in,
                      open(destination_file, "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                return
            os.remove(source_file)
        else:
            if not (
                    os.path.isdir(os.path.join(
                        os.sep.join(path[0:element_of_path + 1]))
                    )
            ):
                os.mkdir(os.path.join(
                    os.sep.join(path[0:element_of_path + 1]))
                )
