# write your code here
import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        print("Incorrect data!")
        return
    if parts[1] == parts[2]:
        print("Same file names!")
        return
    for i, char in enumerate(parts[2]):
        if char == "/":
            paths = parts[2][:i]
            if not os.path.exists(paths):
                os.mkdir(paths)

    with open(parts[1], "r") as file1, open(parts[2], "w") as file2:
        file2.write(file1.read())

    os.remove(parts[1])
