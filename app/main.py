import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    if command_list[0] != "mv" or len(command_list) < 2:
        return

    source_file_name = command_list[1]
    list_of_dirs = command_list[2].split("/")
    list_of_dirs.pop()
    destination_file_name = command_list[2]
    current_path = os.getcwd()

    if list_of_dirs:
        for directory in list_of_dirs:
            new_directory_path = os.path.join(current_path, directory)
            os.makedirs(new_directory_path, exist_ok=True)
            current_path = new_directory_path

    if source_file_name != destination_file_name:
        with (open(source_file_name, "r") as file_in,
              open(destination_file_name, "w") as file_out):
            content = file_in.read()
            file_out.write(content)

        os.remove(source_file_name)
