import os


def move_file(command: str) -> None:
    # That will move a file from one location to another
    # Ex: mv file.txt first_dir/second_dir/third_dir/file2.txt
    if "mv" not in command:
        print("Command mv not found")
        return None
    dir_path = ""
    file_in = command.split(" ")[1]
    file_out = command.split(" ")[2]
    if "/" in file_out:
        dir_ls = file_out.split("/")
        for i in range(len(dir_ls) - 1):
            dir_path += dir_ls[i] + "/"
            os.mkdir(dir_path)
    with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
        f_out.write(f_in.read())
    if os.path.exists(file_in):
        os.remove(file_in)
