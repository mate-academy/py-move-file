from os import rename, path, makedirs, replace


def move_file(line: str) -> None:
    line_lst = line.split()
    if len(line_lst) != 3 or line_lst[0] != "mv":
        raise ValueError("must be: keyword *mv* and two arguments")
    line_src = line_lst[1]
    line_dst = line_lst[2]
    if path.isfile(line_src) is False or not path.split(line_dst)[1]:
        raise ValueError("source file is not exist or error in 2nd argument")
    if path.split(line_src)[0] == path.split(line_dst)[0]:
        rename(line_src, line_dst)
    else:
        head_dst = path.split(line_dst)[0]
        makedirs(head_dst, exist_ok=True)
        if path.isdir(head_dst) is False:
            raise ValueError("can't create directory destination")
        replace(line_src, line_dst)
