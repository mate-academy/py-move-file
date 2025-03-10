import os


def validate_command(command: str) -> None:
    if len(command.split(" ")) != 3:
        raise ValueError("Splited command must have 3 elemnts")
    if "mv" not in command:
        raise ValueError("The first word of the command must be (mv)")
    open(command.split(" ")[1], "r")


def move_file(command: str) -> str:
    try:
        validate_command(command)
    except Exception as ex:
        print(ex)
        return

    origin_content = []
    orgin_file_name = command.split(" ")[1]
    with open(orgin_file_name, "r") as orgin_file:
        for line in orgin_file:
            origin_content.append(line)
    os.remove(str(orgin_file_name))

    file_path = str(command.split(" ")[2])
    if (correct_path := os.path.dirname(file_path)) != "":
        os.makedirs(correct_path, exist_ok=True)

    with open(file_path, "w") as file:
        for line in origin_content:
            file.write(line)
