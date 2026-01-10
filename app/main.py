import os


def move_file(command: str) -> None:
    if not isinstance(command, str):
        print("Incorrect format")
        return

    cmd_list = command.strip().split(" ")

    if len(cmd_list) and cmd_list[0] != "mv":
        print("Command should be 'mv'")
        return

    if len(cmd_list) != 3:
        print("Command 'mv' should contains exactly two arguments")
        return

    source_name = cmd_list[-2]
    destination_name = cmd_list[-1]

    if source_name == destination_name:
        print("Warning: arguments are the same")
        return

    if source_name[-1] == "/":
        print("Warning: source is directory and not a file")
        return

    if destination_name[-1] == "/":
        print("Warning: destination is directory and not a file")
        return

    if not os.path.exists(source_name):
        print("Warning: source file doesn't exist")
        return

    if os.path.exists(destination_name):
        confirm = input("Destination file exists, confirm override (y/n):")
        while confirm not in ["y", "Y", "n", "N"]:
            confirm = input("Destination file exists, confirm override (y/n):")
        if confirm in ["n", "N"]:
            return
        else:
            os.remove(destination_name)

    directory_list = destination_name.split("/")[:-1]
    if not directory_list:
        os.rename(source_name, destination_name)
        return

    path = ""
    for directory in directory_list:
        path += "/" + directory if path else directory
        if not os.path.exists(path):
            os.mkdir(path)

    with open(source_name, "r") as source_file,\
            open(destination_name, "w") as destination_file:
        for line in source_file.readlines():
            destination_file.write(line)

    os.remove(source_name)
