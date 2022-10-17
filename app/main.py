import os


def move_file(command: str) -> None:
    command = command.split(" ")

    source_file = command[1]
    path = command[2].split("/")
    path_final = "/".join(path[:-1])
    os.makedirs(path_final)

    with open(source_file, "r") as source, \
            open(command[2], "w") as file_out:
        file_out.write(source.read())
    os.remove(source_file)


if __name__ == "__main__":
    my_command_line = input("Write command here: ")
    move_file(my_command_line)
