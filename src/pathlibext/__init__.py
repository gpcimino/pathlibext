import os
from pathlib import Path

from pathlibext.find import _find
from pathlibext.rmtree import _rmtree
from pathlibext.shell import _copy
from pathlibext.shell import _copy_preserve_metadata
from pathlibext.shell import _move
from pathlibext.stat import _access_time
from pathlibext.stat import _ctime
from pathlibext.stat import _modification_time
from pathlibext.stat import _size
from pathlibext.tmpdir import _systmpdir
from pathlibext.tmpdir import _tmpdir
from pathlibext.tmpdir import _tmpdir_in
from pathlibext.workdir import _current_file_dir
from pathlibext.workdir import _current_file_path
from pathlibext.tmpfile import _write_text_tmp_file
from pathlibext.tmpfile import _tmp_file

Path.rmtree = _rmtree
Path.find = _find

Path.systmpdir = _systmpdir
Path.tmpdir_in = _tmpdir_in
Path.tmpdir = _tmpdir

Path.size = _size
Path.access_time = _access_time
Path.modification_time = _modification_time

if os.name == "Windows":
    Path.creation_time = _ctime
else:
    Path.metadatachange_time = _ctime

Path.copy = _copy
Path.copy_preserve_metadata = _copy_preserve_metadata
Path.move = _move

Path.current_file_path = _current_file_path
Path.current_file_dir = _current_file_dir

Path.write_text_tmp_file=_write_text_tmp_file
Path.tmp_file=_tmp_file