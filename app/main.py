import os


def move_file(command: str) -> None:
    file_names = command.split()[1:]
    if "/" not in file_names[1]:
        if os.path.exists(file_names[1]):
            os.remove(file_names[1])
        os.rename(file_names[0], file_names[1])
    else:
        second_file_path = file_names[1].split("/")
        second_file_path.pop()
        path_to_second = "/".join(second_file_path)
        if not os.path.exists(path_to_second):
            os.makedirs(path_to_second, exist_ok=True)
        with (
            open(file_names[1], "w") as file_2,
            open(file_names[0], "r") as file_1
        ):
            file_2.write(file_1.read())
        os.remove(file_names[0])
