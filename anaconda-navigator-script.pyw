#!C:/Users/Troley/Anaconda3\pythonw.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'anaconda-navigator==1.4.3','gui_scripts','anaconda-navigator'
__requires__ = 'anaconda-navigator==1.4.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('anaconda-navigator==1.4.3', 'gui_scripts', 'anaconda-navigator')()
    )
