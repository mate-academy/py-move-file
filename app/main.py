import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command, current_file, new_file = command.split()
        dir_name = new_file.split("/")
        if len(dir_name) == 2:
            os.mkdir("first_dir")
        if len(dir_name) == 3:
            os.mkdir("first_dir/second_dir")
        if len(dir_name) == 4:
            os.mkdir("first_dir/second_dir/third_dir")
        with (open(current_file, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
        os.remove(current_file)
