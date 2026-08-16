import os


def move_file(command: str) -> None:

    command_line = command.split(" ")

    if len(command_line) != 3:
        return

    command_op, file_input, file_output \
        = command_line[0], command_line[1], command_line[2]

    if command_op != "mv":
        return

    if (file_output.endswith("/")
            or file_output.endswith("\\")
            or os.path.isdir(file_output)):
        file_output = os.path.join(file_output,
                                   os.path.basename(file_input))

    directory = os.path.dirname(file_output)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with (open(file_input, "r") as file_in,
          open(file_output, "w") as file_out):
        file_out.write(file_in.read())

    os.remove(command_line[1])
