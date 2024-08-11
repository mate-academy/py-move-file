import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3 and command_list[0] == "mv":
        _, source_file, destination_file = command_list
        if not os.path.isdir(destination_file):
            if (os.path.dirname(destination_file)
                    == os.path.dirname(source_file)):
                os.rename(source_file, destination_file)
            else:
                os.makedirs(os.path.dirname(destination_file), exist_ok=True)
                with (open(source_file, "r") as source,
                      open(destination_file, "w") as destiny):
                    destiny.write(source.read())
                os.remove(source_file)
