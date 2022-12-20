import os

with open("file.txt", "w") as f:
    f.writelines(["Some\n", "Text"])


def move_file(command: str) -> None:
    file_split = command.split(" ")
    if "mv" in file_split[0]:
        directory = file_split[2].split("/")
        directories = ""
        if len(directory) > 1:
            for i in range(len(directory) - 1):
                directories += directory[i] + "/"
                os.mkdir(directories)
        with open(file_split[1], "r") as file_in, open(file_split[2], "w") as file_out:
            for line in file_in:
                file_out.write(line)
            os.remove(file_split[1])
