import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) != 3 or command[0] != "mv":
        print("Invalid input format! Make sure the input "
              "string contains 3 elements separated by "
              "space, and has mv on a first place.")
        return

    file_from, file_to = command[1:]

    if "/" in file_to:
        os.makedirs(os.path.dirname(file_to), exist_ok=True)

    try:
        with (open(file_from, "r") as file_in,
              open(file_to, "w") as file_out):
            file_out.write(file_in.read())
        os.remove(f"{file_from}")
    except FileNotFoundError:
        print(f"File {file_from} not found!")
