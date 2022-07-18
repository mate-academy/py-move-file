import os


def move_file(command):
    file_first = command.split()[1]
    file_second = command.split()[2]
    if command.split()[0] == 'mv':
        if "/" in file_second:
            count_dir = file_second.count("/")
            path_file_second = file_second.split("/")
            for i in range(count_dir):
                os.mkdir("/".join(path_file_second[:i + 1]))
        with open(file_first, "r") as file_in, \
                open(file_second, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(file_first)
