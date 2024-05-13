import os


def move_file(command_directory_file: str) -> None:
    cdf = command_directory_file.split()
    if len(cdf) == 3 and cdf[0] == "mv" and cdf[1] != cdf[2]:
        directory = os.path.dirname(cdf[2])
        if os.path.dirname(directory):
            os.makedirs(directory)
        with open(cdf[1], "r") as file_r, open(cdf[2], "w") as file_w:
            file_w.write(file_r.read())
        os.remove(cdf[1])


