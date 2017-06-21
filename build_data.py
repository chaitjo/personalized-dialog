import os
import requests
import shutil

def download(url, path, fname):
    print('downloading ' + fname)
    outfile = os.path.join(path, fname)
    with requests.Session() as session: 
        response = session.get(url, stream=True)
        CHUNK_SIZE = 32768
        with open(outfile, 'wb') as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
        response.close()


def untar(path, fname):
    print('unpacking ' + fname)
    fullpath = os.path.join(path, fname)
    shutil.unpack_archive(fullpath, path)
    os.remove(fullpath)


if __name__ == '__main__':
    dpath = os.path.join('data')
    print('[building data: ' + dpath + ']')
    os.makedirs(dpath, exist_ok=True)
    # Download the data from https://www.dropbox.com/s/4i9u4y24pt3paba/personalized-dialog-dataset.tar.gz?dl=1
    fname = 'personalized-dialog-dataset.tar.gz'
    url = 'https://www.dropbox.com/s/4i9u4y24pt3paba/' + fname + '?dl=1'
    download(url, dpath, fname)
    untar(dpath, fname)
