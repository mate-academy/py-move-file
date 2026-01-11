import os


def move_file(command: str) -> None:
    command = command.split()

    if command[0] != "mv" or len(command) < 3:
        raise NameError("Function only accept 'mv' command")

    start_file = command[1]
    next_file = command[2]

    if next_file.count("/") >= 1:
        file_name = next_file.split("/")[-1]
        os.makedirs(next_file.replace(file_name, ""))

    with open(start_file, "r") as first_file, \
            open(next_file, "w") as second_file:
        text = first_file.read()
        second_file.write(text)


if __name__ == "__main__":
    move_file("mv file.txt file2.txt")
    move_file("mv file.txt first_dir/second_dir/file2.txt")
