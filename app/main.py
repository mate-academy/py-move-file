import os


def move_file(command: str) -> None:
    input_command, path_file_in, path_file_out = command.split(" ")

    if input_command != "mv":
        return

    if "/" not in path_file_out:
        os.rename(path_file_in, path_file_out)
        return

    path_file_out = path_file_out.replace("/", "\\")
    path = "C:\\Programming Study\\Mate\\py-move-file"
    path_file_out_list = path_file_out.split("\\")

    directories_path_file_out = "\\".join(path_file_out_list[:-1])
    absolute_path_file_out = os.path.join(path, directories_path_file_out)

    if not os.path.exists(absolute_path_file_out):
        os.makedirs(absolute_path_file_out)

    absolute_path_file_input = path + "\\" + path_file_in
    absolute_path_file_output = (absolute_path_file_out
                                 + "\\"
                                 + path_file_out_list[-1])

    with (open(absolute_path_file_input, "r") as file_in,
          open(absolute_path_file_output, "w") as file_out):
        read_content = file_in.read()
        file_out.write(read_content)
    os.remove(absolute_path_file_input)
