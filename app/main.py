import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid format. Use: mv <source> <destination>")

    file_out, file_in = parts[1:]

    if not os.path.isfile(file_out):
        raise FileNotFoundError(f"The file '{file_out}' does not exist.")
    
    with open(file_out, "r") as from_file, open(file_in, "w") as to_file:
        to_file.write(from_file.read())

    os.remove(file_out)
