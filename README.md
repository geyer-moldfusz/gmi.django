Setup Django site
-----------------

clone repo

    git clone http://code.neuland.io/gmi/gmi-django.git gmi.django
    cd gmi.django

prepare virtualenv

    virtualenv --python=python3.4 .
    ./bin/pip install zc.buildout

run buildout

   ./bin/buildout

create settings.py

   cp gmi/settings.py.example gmi/settings.py
   vim gmi/settings.py

interact with django

   ./bin/gmi-admin
