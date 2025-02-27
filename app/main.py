import os


def move_file(command: str) -> None:
    split_command = command.split(" ")
    if (len(split_command) < 3
            or split_command[0] != "mv"
            or split_command[1] == split_command[2]):
        return
    path = split_command[2].split("/")
    local_path = ""
    for step in path[:-1]:
        local_path += step
        try:
            os.mkdir(local_path)
        except FileExistsError:
            print("This dir already exists")
        finally:
            local_path += "/"
    try:
        with (open(split_command[1], "r") as file_in,
              open(split_command[2], "w") as file_out):
            file_out.write(file_in.read())
        os.remove(split_command[1])
    except FileNotFoundError:
        print(f"Error: The file '{split_command[1]}' does not exist.")
