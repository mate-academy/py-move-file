import os


def move_file(command: str) -> None:
    if not command[:2] == "mv":
        raise TypeError("Unknown command!")

    list_of_word = command.split()
    file_from = list_of_word[1]
    way_to_file = list_of_word[2]
    dirs = os.path.dirname(way_to_file)

    if dirs:
        os.makedirs(dirs, exist_ok=True)

    with open(file_from, "r") as file_from, open(way_to_file, "w") as file_to:
        for line in file_from:
            file_to.write(line)

    os.remove(list_of_word[1])
