import os


class BadCommand(Exception):
    pass


def move_file(command: str) -> None:
    command_component = command.split(" ")
    if len(command_component) != 3:
        raise BadCommand("Error: the command shall have three components.")
    command_method, old_file, new_file = command_component
    if command_method != "mv":
        raise BadCommand("Error: the command shall start with mv.")
    with open(old_file, "r") as old_file_object:
        old_file_content = old_file_object.read()
    os.remove(old_file)
    directory_list, file_name = os.path.split(new_file)
    if directory_list != "":
        os.makedirs(directory_list, exist_ok=True)
    if file_name == "":
        new_file = os.path.join(directory_list, old_file)
    with open(new_file, "w") as new_file_object:
        new_file_object.write(old_file_content)
