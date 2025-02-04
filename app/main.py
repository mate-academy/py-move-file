import os


def move_file(command: str) -> None:
    command_mv, source, target_path = command.split(" ")
    if not command_mv == "mv":
        raise Exception

    target_dict = target_path.split("/")
    current_path = ""
    if len(target_dict) > 0:
        for index in range(len(target_dict) - 1):
            os.makedirs(f"{current_path}{target_dict[index]}", exist_ok=True)
            current_path += target_dict[index] + "/"

    with open(source, "r") as input, open(target_path, "w") as output:
        output.write(input.read())
    os.remove(source)
