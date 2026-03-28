import os


def move_file(command: str) -> None:
    cmd, file_old, file_new = command.split()
    if cmd == "mv":
        if "/" in file_new:
            directories_list = file_new.split("/")
            file_new = directories_list[-1]
            directories_list = directories_list[0:-1]
            directories = "/".join(directories_list) + "/"
            os.makedirs(directories)
        with open(file_old, "r") as file_in, open(file_new, "w") as file_out:
            file_out.write(file_in.read())
            file_in.close()
            os.remove(f"{file_in}")
            if directories in locals():
                os.replace(f"{file_out}", f"{directories}")
    else:
        raise ValueError
