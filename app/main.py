import os


def move_file(string: str) -> None:
    words = string.split()
    old_file_name = words[1]
    destination_path = os.path.abspath(words[-1])

    new_dir = os.path.dirname(destination_path)

    with open(old_file_name, "r") as source:
        text = source.read()

    os.remove(old_file_name)

    os.makedirs(new_dir, exist_ok=True)

    with open(destination_path, "w") as file:
        file.write(text)
