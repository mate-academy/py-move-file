import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination, filename = os.path.split(parts[2])

    if parts[0] == "mv" and len(parts) == 3:
        if destination and not os.path.exists(destination):
            os.makedirs(destination)
        shutil.copy(source, os.path.join(destination, filename))

    os.remove(source)


if __name__ == "__main__":

    move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")
    print(open("first_dir/second_dir/third_dir/file2.txt").read())
