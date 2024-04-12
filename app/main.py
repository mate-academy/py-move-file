import os


def move_file(command: str) -> None:

    # split command line to have cmd=mv and two files
    cmd_mapped = command.split()

    # check if command has correct syntax
    if (len(cmd_mapped) != 3
            or cmd_mapped[0] != "mv"):
        return

    # split out path to receive list of folder path
    out_file_tree = cmd_mapped[2].split("/")[:-1]

    # run sub folder creation
    tree = ""
    for i in range(len(out_file_tree)):
        tree += out_file_tree[i] + "/"
        if not os.path.isdir(tree[:-1]):
            try:
                os.mkdir(tree[:-1])
            except OSError:
                print(f"failed to create folder {tree[:-1]}")
                return

    # copy source file to destination
    try:
        with (open(cmd_mapped[1], "r") as file_in,
              open(cmd_mapped[2], "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError as filename_err:
        print(f"{filename_err}")
        return
    except OSError:
        print(f"failed to move file {cmd_mapped[1]}")
        return

    # remove source file after successful copy
    try:
        os.remove(cmd_mapped[1])
    except OSError:
        print("can not remove source file. Copied successful.")
        return
