import os


def move_file(command: str):
    try:
        command, original_file, new_file = command.split()
    except ValueError:
        print("Command is incorrect!")

    if not os.path.exists(original_file):
        print("File doesn't exist")
        return

    if new_file.endswith("/"):
        print("This function can move only files, not directories")
        return

    # separate file path and file name for new file
    *path_list, new_file_name = new_file.split("/")

    # creating fpath directories for new file if not exist
    if path_list:
        dir_path = ""
        for i in range(len(path_list)):
            dir_path += path_list[i] + "/"
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

    # copy original file to new file
    with open(original_file) as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())

    # remove original file
    os.remove(original_file)
