import os


def move_file(command):
    split_command = command.split()
    file_source = split_command[1]
    path = split_command[2].split("/")[:-1]

    if len(path) != 0:
        chek_path = True
        build_path = ""
        for dir in path:
            if len(build_path) == 0:
                chek_path = os.path.exists(dir)
                if not chek_path:
                    os.mkdir(dir)
            else:
                chek_path = os.path.exists(build_path + dir)
                if not chek_path:
                    os.mkdir(build_path + dir)
            build_path += dir + "/"

    if not command.endswith("/") or len(path) == 0:
        file_destination = split_command[2]
    else:
        file_destination = split_command[2] + file_source

    try:
        os.replace(file_source, file_destination)
        print(f"File {file_source} moved successfully "
              f"to the destination {file_destination}.")
    except FileNotFoundError:
        print(f"Source file {file_source} does not exist.")
        create = input(f"Create an empty file "
                       f"{file_destination.split('/')[-1]} "
                       f"in the destination folder? y/n: ")
        if create == "y":
            with open(file_destination, "w+"):
                print(f"An empty file {file_destination.split('/')[-1]} "
                      f"was automatically created.")
