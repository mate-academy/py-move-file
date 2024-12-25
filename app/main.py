import os


def move_file(command: str) -> None:
    components = command.split()
    first_part, second_part, third_part = components
    if len(components) == 3 and first_part == "mv":

        file_name = second_part
        path = third_part
        dirs = third_part.split("/")

        if len(dirs) > 1 and len(dirs) != 2:
            current_path = dirs[0]
            if not os.path.exists(current_path):
                os.mkdir(current_path)

            for folder in dirs[1:-1]:
                if folder is not None:
                    current_path = os.path.join(current_path, folder)
                    if not os.path.exists(current_path):
                        os.mkdir(current_path)

            with open(file_name, "r") as file_in, open(path, "w") as file_out:
                content = file_in.read()
                file_out.write(content)
            os.remove(file_name)
        elif len(dirs) == 2:
            current_path = os.path.join(dirs[0], dirs[1])
            with (open(file_name, "r") as file_in,
                  open(current_path, "w") as file_out):
                file_out.write(file_in.read())
            os.remove(file_name)
        elif len(dirs) == 1:
            with (open(file_name, "r") as file_i,
                  open(path, "w") as file_o) :
                file_o.write(file_i.read())
            os.remove(file_name)
