from os import remove, mkdir


def move_file(command: str) -> None:
    mv, input_file, output_file = command.split()
    if "/" not in output_file:
        if input_file == output_file:
            return
        with (open(input_file) as file,
              open(output_file, "w") as result_file):
            result_file.write(file.read())
        remove(input_file)
    else:
        directory = list()
        for folder in output_file.split("/")[:-1]:
            directory.append(folder)
            try:
                mkdir("/".join(directory))
            except OSError:
                continue
        with (open(input_file) as file,
              open(output_file, "w") as result_file):
            result_file.write(file.read())
        remove(input_file)
