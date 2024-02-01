import os


def move_file(command) -> None:
    
    parts = command.split(" ")
    if len(parts) != 3  or parts[0] != "mv":
        raise ValueError("Invalid command")
    
    sourse_file = part[1]

