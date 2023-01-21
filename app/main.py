import os


def move_file(command: str) -> None:
    files_info = command[3:].split(" ")
    first_file = files_info[0]
    second_file_info = files_info[1].split("/")
    if len(second_file_info) == 1:
        os.rename(first_file, second_file_info[0])
    else:
        path = f"{second_file_info[0]}"
        for i in range(1, len(second_file_info)):
            os.mkdir(path)
            path += f"/{second_file_info[i]}"
        with open(first_file, "r") as file_in, open(path, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(first_file)
