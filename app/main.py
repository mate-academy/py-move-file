import os
import shutil


class FileMover:
    def __init__(self, command: str) -> None:
        self.command = command
        self.source = None
        self.destination = None
        self._parse_command()

    def _parse_command(self) -> None:
        parts = self.command.split()

        if len(parts) != 3 or parts[0] != "mv":
            raise ValueError("Invalid command. "
                             "Usage: mv <source> <destination>")

        self.source = parts[1]
        self.destination = parts[2]

    def _validate_source(self) -> None:
        if not os.path.isfile(self.source):
            raise FileNotFoundError(f"Source file "
                                    f"'{self.source}' does not exist.")

    def _prepare_destination(self) -> None:
        if self.destination.endswith("/"):
            os.makedirs(self.destination, exist_ok=True)
            self.destination = os.path.join(self.destination,
                                            os.path.basename(self.source))
        else:
            parent_dir = os.path.dirname(self.destination)
            if parent_dir:
                os.makedirs(parent_dir, exist_ok=True)

    def move(self) -> None:
        self._validate_source()

        self._prepare_destination()

        shutil.move(self.source, self.destination)

        if not os.path.isfile(self.destination):
            raise RuntimeError(f"Failed to move file to '{self.destination}'.")

        if os.path.exists(self.source):
            os.remove(self.source)

    @classmethod
    def move_file(cls, command: str) -> None:
        mover = cls(command)
        mover.move()


def move_file(command: str) -> None:
    FileMover.move_file(command)
