import os


def move_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "mv":
        cmd, input_file, output_file = command.split()
        if "/" in output_file:
            path_to, file_name = os.path.split(output_file)
            os.mkdir(path_to)
            with (
                open(input_file, "r") as in_file,
                open(output_file, "w") as out_file
            ):
                out_file.write(in_file.read())
            os.remove(input_file)
        os.rename(input_file, output_file)
