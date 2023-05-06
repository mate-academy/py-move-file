from os import remove, makedirs, path


def moving_file(input_file: str, output_file: str) -> None:
    with (open(input_file) as file,
          open(output_file, "w") as result_file):
        result_file.write(file.read())
    remove(input_file)


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        mv, input_file, output_file = command.split()
    else:
        raise ValueError("check your command. There are not 3 values")
    if not path.split(output_file):
        if input_file == output_file:
            return
        moving_file(input_file=input_file, output_file=output_file)
    else:
        directory = list()
        for folder in output_file.split("/")[:-1]:
            directory.append(folder)
            makedirs(path.join(*directory), exist_ok=True)
        moving_file(input_file=input_file, output_file=output_file)
