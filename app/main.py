import os


def move_file(command: str) -> None:

    if len(command.split()) == 3:
        cmd, source, destination = command.split()
    else:
        print("The command should have 3 elements ...")
        return

    if cmd != "mv":
        print("Please enter mv command for moving file ...")
        return

    if source == destination:
        print("Doing nothing ...")
        return

    if "/" not in destination:
        os.rename(source, destination)
    else:
        print("Have directory !")
        dirs = destination.split("/")[:-1]
        dest_file_name = destination.split("/")[-1:][0]

        current_dir = ""
        for mydir in dirs:
            current_dir += mydir + "\\"
            path_out_dir = os.path.join(os.getcwd(), current_dir)

            if os.path.exists(current_dir) is not True:
                os.mkdir(path_out_dir)

        path_out = os.path.join(os.path.dirname(path_out_dir), dest_file_name)
        with open(source, "r") as src, open(path_out, "w") as dst:
            dst.write(src.read())

        os.remove(source)
