import os

with open("file.txt", "w") as f:
    f.writelines(["Some\n", "Text"])


def move_file(command: str):
    file = command.split(" ")
    if "mv" in file[0]:
        directory = file[2].split("/")
        directories = ""
        if len(directory) > 1:
            for i in range(len(directory) - 1):
                directories += directory[i] + "/"
                os.mkdir(directories)
        with open(file[1], "r") as file_in, open(file[2], "w") as file_out:
            for line in file_in:
                file_out.write(line)
            os.remove(file[1])


if __name__ == '__main__':
    print(open("file.txt").read())
    move_file("mv file.txt file2.txt")
    print(open("first_dir/second_dir/third_dir/file2.txt").read())
    open("file.txt")
