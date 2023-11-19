import os


def move_files(command: str) -> None:
    list_files = command.split()
    if len(list_files) == 3 and list_files[0] == "mv":
        print(list_files[2])
        path = (list_files[2][0:list_files[2].rindex("/")])
        os.mkdir(f"./{path}")

move_files("mv file.txt first_dir/file2.txt")
