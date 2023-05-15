import os


class PlannedError(Exception):
    """To create os.mkdir("first/second"), first directory needs to exist."""


def move_file(command: str) -> None:
    rename_case_flow = command.split(" ")
    move_case_flow = command.split("/")

    if rename_case_flow[0] != "mv":
        raise ValueError("Wrong command")

    if "/" not in rename_case_flow[2]:
        os.rename(rename_case_flow[1], rename_case_flow[2])

    else:
        source_name = move_case_flow[0].split(" ")[1]
        new_name = move_case_flow[-1]
        path = [f"{move_case_flow[0].split(' ')[2]}"]
        mkdir_path = ""

        for path_component in move_case_flow[1:-1]:
            path.append(path_component)
        for new_folder in range(len(path)):
            try:

                mkdir_path += f"{path[new_folder]}/"
                os.makedirs(mkdir_path)
            except PlannedError:
                print("The path is already created. "
                      "os.makedirs failed as the root directory "
                      "already exists.")

        with (open(f"{source_name}", "r") as source_file,
              open(f"{mkdir_path + new_name}", "w") as file_copy):
            file_copy.write(source_file.read())
        os.remove(f"{source_name}")
