import os


def move_file(command: str) -> None:
    command_list = command.split()
    mv, incoming_file, new_file = command_list
    new_file_list = new_file.split("/")
    dir_path, file_name = os.path.split(new_file)
    if len(command_list) != 3:
        raise IndexError("list index out of range")

    if mv == "mv":
        directory = os.path.join(dir_path)
        if dir_path:
            os.makedirs(directory, exist_ok=True)
        with (
            open(incoming_file, "r") as incoming,
            open(new_file, "w") as new
        ):

            new.write(incoming.read())
        os.replace(incoming_file, new_file_list[-1])
        os.remove(incoming_file)


print(open("file.txt").read())
move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
print(open("first_dir/second_dir/third_dir/file2.txt").read())
