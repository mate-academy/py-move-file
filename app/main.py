import os


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
        for i in move_case_flow[1:-1]:
            path.append(i)
        for i in range(len(path)):
            try:
                mkdir_path += f"{path[i]}/"
                os.mkdir(mkdir_path)
            except Exception as e:
                print(f"{e}")
        with (open(f"{source_name}", "r") as source_file,
              open(f"{mkdir_path + new_name}", "w") as file_copy):
            content = source_file.read()
            file_copy.write(content)
        os.remove(f"{source_name}")
