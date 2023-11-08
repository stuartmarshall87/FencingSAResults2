from pathlib import Path
import re
import os
import filecmp
import shutil

years = ['2015', '2014']
for year in years:
    for path in Path(year).rglob('*.htm'):
        fullpath = path
        path = os.path.basename(path)
        path = os.path.splitext(path)[0]
        if path.endswith('E') or path.endswith('S') or (path.endswith('F') and not (path.endswith('FF') or path.endswith('EF')or path.endswith('SF'))):
            # DO nothing
            a = 1
        else:
            os.remove(fullpath)