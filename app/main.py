from os import remove, mkdir


def move_file(command: str):
    command, file1, file2 = command.split()
    if command != "mv":
        return "Incorrect command"
    if len(file2.split("/")) > 1:
        for i in range(len(file2.split("/") - 1)):
            mkdir(file2.split("/")[i])
    with open(file1, "r") as file_in, open(file2, "w") as file_out:
        file_out.write(file_in.read())

    remove(file1)
