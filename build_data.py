import datetime
import os
import requests
import shutil


def download(url, path, fname, redownload=True):
    """
    Downloads file using `requests`. If ``redownload`` is set to false, then
    will not download tar file again if it is present (default ``True``).
    """
    outfile = os.path.join(path, fname)
    if redownload or not os.path.isfile(outfile):
        with requests.Session() as session:
            response = session.get(url, stream=True)
            CHUNK_SIZE = 32768
            total_size = int(response.headers.get('Content-Length', -1))
            done = 0
            with open(outfile, 'wb') as f:
                for chunk in response.iter_content(CHUNK_SIZE):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                    if total_size > 0:
                        done += len(chunk)
                        if total_size < done:
                            # don't freak out if content-length was too small
                            total_size = done
                        log_progress(done, total_size)
            if done < total_size:
                raise RuntimeWarning('Received less data than specified in ' +
                                     'Content-Length header for ' + url + '.' +
                                     ' There may be a download problem.')
            print()
            response.close()


def log_progress(curr, total, width=40):
    """
    Displays a bar showing the current progress.
    """
    done = min(curr * width // total, width)
    remain = width - done
    progress = '[{}{}] {} / {}'.format(
        ''.join(['|'] * done),
        ''.join(['.'] * remain),
        curr,
        total
    )
    print(progress, end='\r')


def untar(path, fname, deleteTar=True):
    """
    Unpacks the given archive file to the same directory, then (by default)
    deletes the archive file.
    """
    print('unpacking ' + fname)
    fullpath = os.path.join(path, fname)
    shutil.unpack_archive(fullpath, path)
    if deleteTar:
        os.remove(fullpath)


if __name__ == '__main__':
    dpath = os.path.join('data2')

    print('[building data: ' + dpath + ']')
    os.makedirs(dpath, exist_ok=True)

    # Download the data.
    # https://www.dropbox.com/s/4i9u4y24pt3paba/personalized-dialog-dataset.tar.gz?dl=1
    fname = 'personalized-dialog-dataset.tar.gz'
    url = 'https://www.dropbox.com/s/4i9u4y24pt3paba/' + fname + '?dl=1'
    download(url, dpath, fname)
    untar(dpath, fname)