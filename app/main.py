import os


def move_file(command: str) -> None:
    (instruction, file_in, file_out) = command.split()
    print(file_out)

    if "/" in file_out:
        os.makedirs(os.path.dirname(file_out), exist_ok=True)

    with open(file_out, "w") as f1, open(file_in, "r") as f2:
        f1.write(f2.read())

    os.remove(file_in)
