from datetime import datetime
import os

def convert_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{:%Y-%m-%d-%H-%M-%S-%f}.{}'.format(datetime.now(), ext)
    return os.path.join('./videos', filename)

def convert_poster_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{:%Y-%m-%d-%H-%M-%S-%f}.{}'.format(datetime.now(), ext)
    return os.path.join('./posters', filename)