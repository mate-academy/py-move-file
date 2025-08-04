import os.path


def create_folder_path(path: str) -> None:
    ht = os.path.split(path)

    if ht[0] == "":
        if ht[1] != "":
            try:
                os.mkdir(ht[1])
            except OSError:
                print("Creation of the directory %s failed" % ht[1])
    else:
        create_folder_path(ht[0])
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % ht[0])


def move_file(command: str) -> None:
    arr_command = command.split()

    if len(arr_command) != 3:
        print("Invalid command")
        return

    mv, source, destination = arr_command

    if mv != "mv":
        print("Invalid command")
        return

    if source == destination:
        print("Source and destination are the same")
        return

    # check destination
    ht = os.path.split(destination)
    dest_folders = ht[0]
    dest_filename = ht[1] if ht[1] != "" else source
    dest_file_path = os.path.join(dest_folders, dest_filename)

    create_folder_path(dest_folders)

    with open(source, "r") as fr, open(dest_file_path, "w") as fw:
        fw.write(fr.read())

    os.remove(source)
