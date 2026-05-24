# write your code here
import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    command_name, source_file, destination_path = parts
    if command_name != "mv":
        return
    if not os.path.exists(source_file):
        return
    if destination_path.endswith("/"):
        destination_path = os.path.join(destination_path, source_file)
    directory = os.path.dirname(destination_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    with open(source_file, "r") as file_in, \
         open(destination_path, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(source_file)
