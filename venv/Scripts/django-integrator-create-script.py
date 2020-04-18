#!F:\Projects\PyCharm\django_test\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Django-Integrator==1.1.1.1','console_scripts','django-integrator-create'
__requires__ = 'Django-Integrator==1.1.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Django-Integrator==1.1.1.1', 'console_scripts', 'django-integrator-create')()
    )
