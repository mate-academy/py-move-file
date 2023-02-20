import os


def move_file(command: str) -> None:
    mv_command, source_file, new_file_path = command.split()
    if mv_command == "mv":
        path = new_file_path.split("/")
        new_file_name = path[-1]
        path = path[:-1]
        if not path:
            real_new_file_path = new_file_name
        else:
            made_directory = ""
            for directory in path:
                if made_directory:
                    path_to_directory = os.path.join(made_directory, directory)
                else:
                    path_to_directory = directory
                if not os.path.exists(path_to_directory):
                    os.mkdir(path_to_directory)
                made_directory = path_to_directory
            real_new_file_path = os.path.join(path_to_directory, new_file_name)
    with open(source_file, "r") as source, open(
        real_new_file_path, "w"
    ) as new_file:
        new_file.write(source.read())
    os.remove(source_file)
