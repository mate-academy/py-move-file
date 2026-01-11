from app.context_manager import MoveFileManager


def copy_content_file_to_file(
        source_file: str,
        file_copy: str
) -> None:
    with (open(source_file, "r") as sf,
          open(file_copy, "w") as fc):
        fc.write(sf.read())


def manager_call(
        source_file: str,
        moved_file: str,
        path: str
) -> None:
    with MoveFileManager(source_file, path):
        copy_content_file_to_file(source_file, moved_file)
