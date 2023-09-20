import os


def move_file(command: str) -> None:
    mv, input_name, output_name = command.split(" ")

    if mv != "mv":
        return
    with open(input_name, "r") as file:
        text = file.read()
    os.remove(input_name)

    file_path = output_name.split("/")
    print(file_path)
    current = ""

    if file_path[0] != "":
        for directory in file_path[:-1]:
            current = os.path.join(current, directory)
            if not os.path.exists(current):
                os.mkdir(current)

    with open(output_name, "w") as file:
        file.write(text)
