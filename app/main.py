import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Comando inválido")

    src = parts[1]
    dst = parts[2]

    if not os.path.isfile(src):
        raise FileNotFoundError("Arquivo não encontrado: " + src)

    dst = dst.replace("\\", "/")

    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))

    dst_dir = os.path.dirname(dst)

    if dst_dir:
        path_parts = dst_dir.split("/")
        current = ""
        for paths in path_parts:
            if paths == "":
                continue
            current = os.path.join(current, paths)
            if not os.path.exists(current):
                os.mkdir(current)

    with open(src, "rb") as fsrc:
        data = fsrc.read()

    with open(dst, "wb") as fdst:
        fdst.write(data)

    os.remove(src)
