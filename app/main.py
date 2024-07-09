# write your code here
import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "mv" and parts[1] != parts[2]:
        source = parts[1]
        dest = parts[2]

        if os.path.isdir(dest) or dest.endswith("/"):
            dest = os.path.join(dest, source)
        if os.path.dirname(dest):
            os.makedirs(os.path.dirname(dest), exist_ok=True)

        os.rename(source, dest)
