import os
from os.path import join, expanduser
# If on Linux get, /home/$USER
# If on Windows get, c:\\Users\\MyUser
HOME = expanduser("~")

PATH = join(HOME, '.pygalume')

if not os.path.isdir(PATH):
    os.makedirs(PATH)

DATABASE_URL = join(PATH, 'banco.db')

API_URL = 'http://api.vagalume.com.br/search.php?'
