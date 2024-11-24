import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3 and command_list[0] == "mv":
        old_name, new_name = command_list[1:]
        if "/" not in new_name:
            pass
        else:
            new_name_split = new_name.split("/")
            path = new_name_split[0]
            for index in range(1, len(new_name_split)):
                if os.path.exists(path) is False:
                    os.makedirs(path)
                    path += f"/{new_name_split[index]}"

                else:
                    path += f"/{new_name_split[index]}"
            #     print(path)
            # print(path)
        with (open(old_name, "r") as input_file,
              open(new_name, "w") as output_file):
            output_file.write(input_file.read())
            os.remove(old_name)
