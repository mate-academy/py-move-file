import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        cm, first_file, second_file = command.split()
        if cm == "mv" and first_file != second_file:
            if "/" not in second_file:
                create_file(first_file, second_file)
            else:
                directory = second_file.split("/")[0:-1]
                os.makedirs(os.path.join(*directory), exist_ok=True)
                create_file(first_file, second_file)
    else:
        raise Exception("wrong type of command")


def create_file(
        first_file_name: str,
        second_file_name: str
) -> None:
    with (
        open(first_file_name, "r") as file_remove,
        open(second_file_name, "w") as file_create
    ):
        file_create.write(file_remove.read())

    os.remove(first_file_name)
