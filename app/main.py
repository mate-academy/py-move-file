import os


def move_file(command: str):
    if "mv" not in command:
        raise MvError("mv not in `command`")

    split_file = command.split(" ")
    if split_file[0] != "mv":
        raise IfMvNotFirstIndex("mv not the first index in list `split_file`")
    else:
        first_file = split_file[1]
        with open(first_file, "r") as file_out:
            text = file_out.read()

        second_file_with_path = split_file[2]
        path_element = second_file_with_path.split("/")[-1]

        for file_name in path_element:
            path = f"{file_name}/"
            os.makedirs(path)

        with open(second_file_with_path, "w") as file_in:
            file_in.write(text)

        os.remove(first_file)


class MvError(Exception):
    pass


class IfMvNotFirstIndex(Exception):
    pass
