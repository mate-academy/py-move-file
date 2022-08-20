import os


def move_file(command: str):
    command = command.split()
    original_name = command[1]
    file_name_and_path = command[-1]

    # If we have a path for a new file
    if "/" in file_name_and_path:
        path_and_file = file_name_and_path.split("/")
        copy_name = path_and_file[-1]
        file_path = path_and_file[0:-1]
        previous_directories = ""
        for directory in file_path:
            if previous_directories == "":
                os.mkdir(directory)
                previous_directories = previous_directories + directory + "/"
            else:
                os.mkdir(previous_directories + directory)
                previous_directories = previous_directories + directory + "/"

        file_path = "/".join(file_path)
        with open(original_name, "r") as origin, \
                open(file_path + "/" + copy_name, "w") as copy:
            [copy.write(line) for line in origin]

        os.remove(original_name)

    # Renaming the file
    else:
        os.rename(original_name, file_name_and_path)
