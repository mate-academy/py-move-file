import os


def move_file(command: str) -> None:
    string = list(command.split())
    if len(string) != 3:
        raise ValueError("Error arguments")
    command_from_string, file_in, file_out = string
    if command_from_string == "mv":
        if "/" not in file_out:
            os.rename(file_in, file_out)
        if "/" in file_out:
            path = ""
            while "/" in file_out:
                new_directory = file_out[0:(file_out.find("/"))]
                path = os.path.join(path, new_directory)
                if not os.path.isdir(path):
                    os.mkdir(path)
                file_out = file_out[(file_out.find("/")) + 1:]
            if file_out == ".txt":
                file_out = file_in
            with open(file_in, "r") as file1, \
                    open(os.path.join(path, file_out), "w") as file2:
                content = (file1.read())
                file2.write(content)
            os.remove(file_in)
