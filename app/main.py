import os


def move_file(command: str) -> None:
    command_elements = command.split()

    if len(command_elements) != 3 or command_elements[0] != "mv":
        return

    _, source, destination = command_elements

    if "/" not in destination:
        os.rename(source, destination)
        return

    directories = destination.split("/")
    new_file_name = source
    if directories[-1]:
        new_file_name = directories.pop(-1)
    else:
        directories.pop(-1)

    checked_path = ""
    for dir_name in directories:
        checked_path = os.path.join(checked_path, dir_name)
        if not os.path.exists(checked_path):
            os.mkdir(checked_path)

    final_destination = os.path.join(checked_path, new_file_name)

    with (open(source, "r") as file_in,
          open(final_destination, "w") as file_out):
        file_out.write(file_in.read())

    os.remove(source)
