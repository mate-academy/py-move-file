import os


def move_file(command: str) -> None:
    file1 = command.split(" ")[1]
    file2_path = command.split(" ")[2]

    for i in range(file2_path.count("/")):
        path = "/".join(file2_path.split("/")[:i + 1])
        if os.path.exists(path):
            continue
        os.mkdir(path)

    with open(file1, "r") as f1, open(file2_path, "w") as f2:
        f2.write(f1.read())
    os.remove(file1)
