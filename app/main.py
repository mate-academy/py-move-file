import os


def move_file(command: str) -> None:
    list_of_command = command.split(" ")
    if os.path.dirname(list_of_command[2]) != "":
        os.makedirs(os.path.dirname(list_of_command[2]), exist_ok=True)
        with (open(list_of_command[2], "w", encoding="utf-8") as file_to,
              open(list_of_command[1], "r", encoding="utf-8") as file_from):
            file_to.write(file_from.read())
    else:
        with (open(list_of_command[2], "w", encoding="utf-8") as file_to,
              open(list_of_command[1], "r", encoding="utf-8") as file_from):
            file_to.write(file_from.read())
    os.remove(list_of_command[1])
