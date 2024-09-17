import os


def move_file(command: str) -> None:
    command = command.split()
    command[2] = command[2].split("/")
    command.append(command[2][-1])
    current_file = command[1]
    directory = "/".join(command[2][:-1])
    new_file = command[-1]

    if directory != '':
        os.makedirs(directory)
        directory += '/'
    with (open(current_file, "r") as old_file,
          open(f"{directory}{new_file}", "w") as new_file):
        new_file.write(old_file.read())
    os.remove(current_file)
