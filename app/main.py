import os


def move_file(command: str):
    destination = []
    directory = ""
    files = command.split()
    if "/" in files[2]:
        destination = files[2].split("/")
    for i in range(len(destination) - 1):
        directory += destination[i] + "/"
        os.mkdir(directory)
    with open(files[1], "r") as file_input,\
         open(files[2], "w") as file_output:
        text = file_input.read()
        file_output.write(text)
    os.remove(files[1])
