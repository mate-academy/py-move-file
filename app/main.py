from os import path, mkdir, chdir, curdir, rename


def move_file(command: str) -> None:
    args = command.split()
    root_dir = path.abspath(curdir)
    if (len(args) == 3 and args[0] == "mv" and args[2] != args[1]):
        dest_path = args[2].split("/")
        if len(dest_path) > 1:
            for i in range(len(dest_path) - 1):
                if not path.exists(dest_path[i]):
                    mkdir(dest_path[i])
                chdir("./" + dest_path[i])
        chdir(root_dir)
        rename(args[1], "./" + args[2])
