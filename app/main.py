import os


def move_file(command: str) -> None:
    commands = command.split(maxsplit=2)
    if len(commands) != 3 or commands[0] != "mv":
        raise ValueError("Invalid command format:"
                         " expected 'mv <source> <destination>'")

    _, src, dst = commands

    if not os.path.isfile(src):
        raise FileNotFoundError(f"Source file not found: {src}")

    # Verificar se destino termina com / (é um diretório)
    if dst.endswith("/") or dst.endswith(os.sep):
        dest_path = os.path.join(dst, os.path.basename(src))
    else:
        dest_path = dst

    # Criar diretórios necessários progressivamente
    dirpath = os.path.dirname(dest_path)
    if dirpath:
        current = ""
        for part in dirpath.split(os.sep):
            if not part:
                continue
            current = os.path.join(current, part) if current else part
            if not os.path.exists(current):
                try:
                    os.mkdir(current)
                except FileExistsError:
                    pass

    # Copiar o arquivo em blocos
    block_size = 4096
    with open(src, "rb") as fsrc:
        with open(dest_path, "wb") as fdst:
            while True:
                block = fsrc.read(block_size)
                if not block:
                    break
                fdst.write(block)

    # Remover arquivo original
    os.remove(src)
