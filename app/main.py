import os

with open("file.txt", "w") as f:
    f.writelines(["Some\n", "Text"])


def move_file(command: str) -> None:
    f_split = command.split(" ")
    if "mv" in f_split[0]:
        directory = f_split[2].split("/")
        directories = ""
        if len(directory) > 1:
            for i in range(len(directory) - 1):
                directories += directory[i] + "/"
                os.mkdir(directories)
        with open(f_split[1], "r") as f_in, open(f_split[2], "w") as f_out:
            for line in f_in:
                f_out.write(line)
            os.remove(f_split[1])
