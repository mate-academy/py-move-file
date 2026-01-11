import os


def validate_command(command: str) -> None:
    if len(command.split(" ")) != 3:
        raise ValueError("Split command must have 3 elements")
    if command.split(" ")[0] != "mv":
        raise ValueError("The first word of the command must be (mv)")
    open(command.split(" ")[1], "r")


def move_file(command: str) -> str:
    try:
        validate_command(command)
    except Exception as ex:
        print(ex)
        return

    origin_file_name = command.split(" ")[1]
    destination_path = str(command.split(" ")[2])
    if destination_path[-1] == "/":
        destination_path += origin_file_name

    with open(origin_file_name, "r") as origin_file:
        origin_content = origin_file.readlines()
    os.remove(str(origin_file_name))

    destination_dir = os.path.dirname(destination_path)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    destination_file = os.path.join(destination_dir, os.path.basename(destination_path))  # noqa: E501
    with open(destination_file, "w") as file:
        file.writelines(origin_content)
