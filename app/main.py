import os


def move_file(command: str) -> None:
    parsed_command = command.split(" ")
    if len(parsed_command) != 3 or parsed_command[0] != "mv":
        return
    com, source, destination = parsed_command
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    if "/" in destination:
        os.makedirs(os.path.dirname(destination), exist_ok=True)
    with open(source) as old_file:
        content = old_file.read()
    with open(destination, "w") as new_file:
        new_file.write(content)
    os.remove(source)
