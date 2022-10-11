import os


def move_file(command: str) -> None:
    command = command.split()

    if command[0] != "mv" or len(command) < 3:
        raise NameError("Function only accept 'mv' command")

    old_file = command[1]
    new_file = command[2]

    if new_file.count("/") >= 1:
        file_name = new_file.split("/")[-1]
        os.makedirs(new_file.replace(file_name, ""))

    with open(old_file, "r") as in_file, open(new_file, "w") as out_file:
        out_file.write(in_file.read())


if __name__ == "__main__":
    move_file("mv file.txt file2.txt")
    move_file("mv file.txt first_dir/second_dir/file2.txt")
