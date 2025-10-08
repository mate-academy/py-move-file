import os


def _make_dirs_one_by_one(path: str) -> None:
    """
    Cria diretórios de forma incremental, garantindo que cada nível exista.

    Exemplo:
        _make_dirs_one_by_one("first/second/third")
    """
    parts = path.split(os.path.sep)
    current = ""
    for part in parts:
        if not part:
            continue
        current = os.path.join(current, part)
        if not os.path.exists(current):
            os.mkdir(current)


def move_file(command: str) -> None:
    """
    Move um arquivo conforme o comportamento básico do comando `mv`.

    Exemplo:
        move_file("mv file.txt dir/subdir/new_name.txt")

    A função:
        - Valida o comando.
        - Cria diretórios intermediários com os.mkdir().
        - Lê o arquivo de origem.
        - Cria o arquivo de destino.
        - Remove o arquivo original.
    """
    parts = command.split()

    # Validação básica do comando
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Command invalid")

    src = parts[1]
    dest_original = parts[2]

    # Normaliza os caminhos (para evitar erros de barras invertidas)
    src = os.path.normpath(src)
    dest = os.path.normpath(dest_original)

    # Evita mover o arquivo para ele mesmo
    if os.path.abspath(src) == os.path.abspath(dest):
        return

    # Caso o destino termine com "/", é tratado como diretório
    if (
        dest_original.endswith("/")
        or dest_original.endswith(os.path.sep)
        or os.path.isdir(dest)
    ):
        dest_dir = dest
        if (
            dest_dir not in ("", ".", os.path.sep)
            and not os.path.exists(dest_dir)
        ):
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

    # Verifica se o arquivo de origem existe
    if not os.path.isfile(src):
        raise FileNotFoundError(f"No such file: '{src}'")

    # Lê o conteúdo do arquivo de origem
    with open(src, "rb") as file_src:
        data = file_src.read()

    # Garante que o diretório de destino exista antes de criar o novo arquivo
    dest_dir = os.path.dirname(dest)
    if dest_dir and not os.path.exists(dest_dir):
        _make_dirs_one_by_one(dest_dir)

    # Cria o novo arquivo de destino e escreve os dados
    with open(dest, "wb") as file_dest:
        file_dest.write(data)

    # Remove o arquivo de origem após mover
    os.remove(src)
