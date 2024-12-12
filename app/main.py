import os


def move_file(string: str) -> None:
    words = string.split()
    if len(words) != 3:
        raise TypeError
    elif words[0] != "mv":
        raise ValueError

    old_file_name = words[1]

    if words[-1][-1] == "\\" or words[-1][-1] == "/":
        destination_path = os.path.join(*words[-1])
        os.makedirs(destination_path, exist_ok=True)
        return None
    else:
        destination_path = os.path.join(*words[-1].split("/"))

    new_dir = os.path.dirname(destination_path)

    with open(old_file_name, "r") as source:
        text = source.read()

    os.remove(old_file_name)

    if new_dir:
        os.makedirs(new_dir, exist_ok=True)
    else:
        with open(destination_path, "w") as file:
            file.write(text)

    with open(destination_path, "w") as file:
        file.write(text)
