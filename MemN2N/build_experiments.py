import os
import requests
import shutil

def download(url, fname):
    print('downloading ' + fname)
    outfile = os.path.join(fname)
    with requests.Session() as session: 
        response = session.get(url, stream=True)
        CHUNK_SIZE = 32768
        with open(outfile, 'wb') as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
        response.close()


def untar(fname):
    print('unpacking ' + fname)
    fullpath = os.path.join(fname)
    shutil.unpack_archive(fullpath)
    os.remove(fullpath)


if __name__ == '__main__':
    print('[building experimental data]')
    # Download the data from https://www.dropbox.com/s/uhp7u5kmtyrbvkh/runs.tar.gz?dl=1
    fname = 'runs.tar.gz'
    url = 'https://www.dropbox.com/s/uhp7u5kmtyrbvkh/' + fname + '?dl=1'
    download(url, fname)
    untar(fname)
