#!e:\marci\obudai_egyetem\allasinteju_kerdesek\datapao\imdb-scraper\.venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'cinemagoer==2022.2.11','console_scripts','imdbpy'
__requires__ = 'cinemagoer==2022.2.11'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('cinemagoer==2022.2.11', 'console_scripts', 'imdbpy')()
    )
