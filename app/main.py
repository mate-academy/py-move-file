import os


def move_file(mv: str) -> None:
    if len(mv.split()) != 3:
        return
    mv, source_file, new_file = mv.split()
    if "/" not in new_file:
        with open(new_file, "w") as n_file, open(source_file) as s_file:
            n_file.write(s_file.read())
    elif new_file[-1] == "/":
        oll_dir = str(new_file[:-1])
        with_first_dir = ""
        for current_dir in oll_dir.split("/"):
            with_first_dir = os.path.join(with_first_dir, current_dir)
            if os.path.exists(with_first_dir):
                os.mkdir(with_first_dir)
        with open(os.path.join(with_first_dir, new_file), "w") as n_file, \
                open(source_file) as s_file:
            n_file.write(s_file.read())
    else:
        oll_dir = str(new_file)
        new_file = oll_dir.split("/")[-1]
        with_first_dir = ""
        for current_dir in oll_dir.split("/")[:-1]:
            with_first_dir = os.path.join(with_first_dir, current_dir)
            if not os.path.isdir(with_first_dir):
                os.mkdir(with_first_dir)
        with open(os.path.join(with_first_dir, new_file), "w") as n_file,\
                open(source_file) as s_file:
            n_file.write(s_file.read())
    os.remove(source_file)
