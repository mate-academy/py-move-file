import os


def move_file(command: str) -> None | str:
    files = command.split(" ")
    if len(files) != 3 or files[0] != "mv":
        return "Invalid command"
    source_file = files[1]
    destination_file = files[2]
    if len(destination_file.split("/")) > 1:
        os.makedirs("/".join(destination_file.split("/")[:-1]), exist_ok=True)
    with open(destination_file, "w") as new_file, \
         open(source_file, "r") as old_file:
        new_file.write(old_file.read())
    os.remove(files[1])
