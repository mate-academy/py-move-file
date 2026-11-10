import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) < 3:
        return
    elif command_list[0] != "mv":
        return
    elif command_list[2].find("/") == -1:
        if os.path.isfile(command_list[1]):
            if os.path.isdir(command_list[2]):
                destination = str(command_list[2]) + str(command_list[1])
                with open(command_list[1], "r") as file_in:
                    content = file_in.read()
                with open(destination, "w") as file_out:
                    file_out.write(content)
                os.remove(command_list[1])
            else:
                with open(command_list[1], "r") as file_in:
                    content = file_in.read()
                with open(command_list[2], "w") as file_out:
                    file_out.write(content)
                os.remove(command_list[1])
    elif command_list[2][-1] == "/":
        if os.path.isfile(command_list[1]):
            if os.path.isdir(command_list[2]):
                destination = str(command_list[2]) + str(command_list[1])
                with open(command_list[1], "r") as file_in:
                    content = file_in.read()
                with open(destination, "w") as file_out:
                    file_out.write(content)
                os.remove(command_list[1])
            else:
                file_path = str(command_list[2]) + str(command_list[1])
                with open(command_list[1], "r") as file_in:
                    content = file_in.read()
                with open(file_path, "w") as file_out:
                    file_out.write(content)
                os.remove(command_list[1])
    elif os.path.isfile(command_list[1]):
        new_file_path = command_list[2].split("/")
        for i in range(len(new_file_path) - 1):
            partial_path = "/".join(new_file_path[:i + 1])
            if not os.path.exists(partial_path):
                os.makedirs(partial_path, exist_ok=True)

        if os.path.isdir(command_list[2]):
            destination = str(command_list[2]) + str(command_list[1])
            with open(command_list[1], "r") as file_in:
                content = file_in.read()
            with open(destination, "w") as file_out:
                file_out.write(content)
            os.remove(command_list[1])
        else:
            with open(command_list[1], "r") as file_in:
                content = file_in.read()
            with open(command_list[2], "w") as file_out:
                file_out.write(content)

            os.remove(command_list[1])
