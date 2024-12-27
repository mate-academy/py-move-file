from os import mkdir, replace
import os


def move_file(command):
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv <source> <destination>")

    source = parts[1]
    destination = parts[2]

    three = destination.split("/")
    array = []
    for i in range(0, len(three)-1):
        array.append(three[i])
        if not os.path.exists("/".join(array)):
            mkdir("/".join(array))

    replace(source, destination)


#move_file('mv file.txt first_dir/second_dir/third_dir/file2.txt')