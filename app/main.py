import os


def create_directory(directory_list: list) -> str:
    path_to_file = ""
    for directory in directory_list:
        path_to_file = os.path.join(path_to_file, directory)
        if not os.path.exists(path_to_file):
            os.mkdir(path_to_file)
    return path_to_file


def move_file(command: str) -> None:
    mv_command, source_file, new_file_path = command.split()
    if mv_command == "mv":
        path = new_file_path.split("/")
        new_file_name = path.pop()
        if path:
            path_to_directory = create_directory(path)
            real_new_file_path = os.path.join(path_to_directory, new_file_name)
        else:
            real_new_file_path = new_file_name
    with open(source_file, "r") as source, open(
        real_new_file_path, "w"
    ) as new_file:
        new_file.write(source.read())
    os.remove(source_file)
