import os


def move_file(command: str) -> None:
    list_command = command.split(" ")

    first_file = list_command[1]

    mv_file_path = list_command[2].split("/")

    second_filename = ""

    for index in range(len(mv_file_path)):
        if ".txt" in mv_file_path[index]:
            second_filename += mv_file_path[index]
            mv_file_path.pop(index)

    with open(first_file, "r"), open(second_filename, "w"):
        path1 = ""
        for path in mv_file_path:
            path1 += path + "/"
            os.mkdir(path1)

        os.rename(first_file, path1 + second_filename)

        if len(path1) != 0:
            os.remove(second_filename)
