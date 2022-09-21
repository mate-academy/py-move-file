import os


def move_file(command: str) -> None:
    command = command.split()[1:]
    if "/" in command[1]:
        directory = command[1][:command[-1].rindex("/")]
        os.makedirs(directory)
        with open(command[0], "r") as original_file,\
                open(command[1], "w") as moved_file:
            for text in original_file.read():
                moved_file.write(text)
        os.remove(command[0])
    else:
        os.rename(command[0], command[1])
