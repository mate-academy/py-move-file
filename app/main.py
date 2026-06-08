import os


def move_file(command: str) -> None:
    try:
        cm, file_input, file_output = command.strip().split(" ")
    except ValueError:
        return
    if cm != "mv":
        return

    file_output_dir = os.path.dirname(file_output)
    if file_output_dir == "":
        os.rename(file_input, file_output)
        return

    file_output_name = os.path.basename(file_output)
    if file_output_name == "":
        file_output_name = file_input

    current_dir = ""
    print(file_output_dir.split("/"))
    for folder in file_output_dir.split("/"):
        current_dir = os.path.join(current_dir, folder)
        if not os.path.exists(current_dir):
            os.mkdir(current_dir)
    with (open(file_input, "r") as file_in,
          open(os.path.join(file_output_dir, file_output_name), "w")
          as file_out):
        file_out.write(file_in.read())
    os.remove(file_input)
