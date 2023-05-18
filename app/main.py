import os


def move_file(command: str) -> None:
    elements = command.split()
    if len(elements) == 3:
        command, file_in, file_path = elements
        if command == "mv":
            path_elements = file_path.split("/")
            path = path_elements[0]
            for element in path_elements[1:]:
                if not os.path.isdir(path):
                    os.mkdir(path)
                path += "/" + element
            with open(file_in, "r") as f_in, open(path, "w") as f_out:
                f_out.write(f_in.read())
            os.remove(file_in)
