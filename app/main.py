import os


def move_file(command: str) -> None:
    if (
            len(cmd_chain := command.split(" ")) == 3
            and cmd_chain[0] == "mv"
            and os.path.exists(cmd_chain[1])
            and not cmd_chain[2].startswith(("--", "/", "../"))
    ):
        src, dst = cmd_chain[1], cmd_chain[2]
        *parent, base = dst.split("/")

        if parent:
            os.makedirs("/".join(parent), exist_ok=True)

        if not base or os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))

        with (
            open(src, "rb") as file_in,
            open(dst, "wb") as file_out
        ):
            file_out.write(file_in.read())

        os.remove(src)
        print("File moved successfully.")
