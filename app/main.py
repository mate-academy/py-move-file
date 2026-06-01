import os


def move_file(command: str) -> None:
    order, source, directory = command.split()
    path = directory.split("/")
    current_path: str = ""

    if order == "mv":

        for folder in path[:-1]:
            current_path = os.path.join(current_path, folder)

            if not os.path.isdir(current_path):
                os.mkdir(current_path)

        with open(directory, "w") as final:
            with open(source, "r") as s:
                final.write(s.read())
            os.remove(source)
    else:
        return


if __name__ == "__main__":
    move_file("mv file.txt first_dir/second_dir/file2.txt")
