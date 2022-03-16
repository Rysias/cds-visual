import re
from shutil import copyfile
from pathlib import Path

notebook_files = Path("notebooks").glob("session*rdkm.ipynb")
latest_file = max(notebook_files, key=lambda x: x.lstat().st_mtime)

filenum = int(re.search("\d+", latest_file.name).group())

new_file = Path("notebooks") / f"session{filenum}_jhr.ipynb"

if not new_file.exists():
    copyfile(latest_file, new_file)

