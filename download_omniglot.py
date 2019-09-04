'''Download omniglot data set.'''

import shutil
from pathlib import Path
from urllib.request import urlopen
from tempfile import TemporaryDirectory

IMAGES_BACKGROUND = 'https://github.com/brendenlake/omniglot/blob/master/python/images_background.zip?raw=true'
IMAGES_EVALUATION = 'https://github.com/brendenlake/omniglot/blob/master/python/images_evaluation.zip?raw=true'


def download(url, dest):
    '''Download a file and write to dest.'''
    with urlopen(url) as response, open(dest, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


def main(data_dir):
    data_dir = Path(data_dir)
    data_dir.mkdir()
    with TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        download(IMAGES_BACKGROUND, tmp_dir / 'images_background.zip')
        download(IMAGES_EVALUATION, tmp_dir / 'images_evaluation.zip')
        shutil.unpack_archive(tmp_dir / 'images_background.zip', data_dir)
        shutil.unpack_archive(tmp_dir / 'images_evaluation.zip', data_dir)
    for data in (data_dir / 'images_background').iterdir():
        shutil.move(str(data), str(data_dir))
    for data in (data_dir / 'images_evaluation').iterdir():
        shutil.move(str(data), str(data_dir))
    shutil.rmtree(data_dir / 'images_background')
    shutil.rmtree(data_dir / 'images_evaluation')


if __name__ == '__main__':
    main('data/omniglot/data')
