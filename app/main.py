import os


def move_file(mv_file: str) -> None:
    create_list = mv_file.split()
    if len(create_list) < 3 or create_list[0] != "mv":
        raise FileNotFoundError
    if "/" not in mv_file:
        with open(create_list[1], "r") as read_file, open(create_list[-1], "w") as create_file:
            create_file.write(read_file.read())
            if create_list[1] != create_list[-1]:
                os.remove(create_list[1])
    else:
        create_folder = create_list[-1].replace("/", ",").split(",")
        current_path = ""
        for folder in create_folder[:-1]:
            current_path = os.path.join(current_path, folder)
            if not os.path.exists(current_path):
                os.mkdir(current_path)
        if os.path.exists(current_path):
            if create_folder[-1].endswith(".txt"):
                with open(create_list[1], "r") as read_file, open(f"{current_path}/{create_folder[-1]}", "w") as create_file:
                    create_file.write(read_file.read())
                    os.remove(create_list[1])
