import os


def _make_dirs_one_by_one(path: str) -> None:
    """
    Cria diretórios de forma incremental, garantindo que cada nível exista.
    Funciona com caminhos relativos e absolutos, incluindo Windows e Linux.
    """
    if not path:
        return

    # Detecta caminho absoluto e inicializa corretamente
    if os.path.isabs(path):
        drive, tail = os.path.splitdrive(path)
        current = drive + os.path.sep
        parts = tail.strip(os.path.sep).split(os.path.sep)
    else:
        current = ""
        parts = path.strip(os.path.sep).split(os.path.sep)

    for part in parts:
        if not part:
            continue
        current = os.path.join(current, part)
        if not os.path.exists(current):
            os.mkdir(current)
        elif not os.path.isdir(current):
            raise NotADirectoryError(
                f"Path exists and is not a directory: {current}"
            )


def move_file(command: str) -> None:
    """
    Move um arquivo conforme o comportamento básico do comando `mv`.

    Exemplo:
        move_file("mv file.txt dir/subdir/new_name.txt")

    A função:
        - Valida o comando usando unpacking
        - Cria diretórios intermediários com os.mkdir()
        - Lê o arquivo de origem
        - Cria o arquivo de destino
        - Remove o arquivo original
    """
    try:
        cmd_token, src, dest_original = command.split()
    except ValueError:
        raise ValueError("Command invalid")

    if cmd_token != "mv":
        raise ValueError("Command invalid")

    # Normaliza caminhos
    src = os.path.normpath(src)
    dest = os.path.normpath(dest_original)

    # Resolve destino final (considerando diretórios)
    if (
        dest_original.endswith("/")
        or dest_original.endswith(os.path.sep)
        or os.path.isdir(dest)
    ):
        dest_dir = dest
        if dest_dir not in ("", ".", os.path.sep) and not os.path.exists(dest_dir):
            _make_dirs_one_by_one(dest_dir)
        dest = os.path.join(dest_dir, os.path.basename(src))
    else:
        dest_dir = os.path.dirname(dest) or "."
        if os.path.exists(dest_dir) and not os.path.isdir(dest_dir):
            raise NotADirectoryError(
                f"Destination exists and is not a directory: {dest_dir}"
            )
        if dest_dir not in (".", "") and not os.path.exists(dest_dir):
            _make_dirs_one_by_one(dest_dir)

    # Agora podemos comparar src e dest com segurança
    if os.path.abspath(src) == os.path.abspath(dest):
        return

    # Verifica se arquivo de origem existe
    if not os.path.isfile(src):
        raise FileNotFoundError(f"No such file: '{src}'")

    # Lê conteúdo do arquivo de origem
    with open(src, "rb") as file_src:
        data = file_src.read()

    # Garante que diretório de destino exista
    dest_dir = os.path.dirname(dest)
    if dest_dir and not os.path.exists(dest_dir):
        _make_dirs_one_by_one(dest_dir)

    # Cria arquivo de destino e escreve dados
    with open(dest, "wb") as file_dest:
        file_dest.write(data)

    # Remove arquivo de origem
    os.remove(src)
