import urllib
import linecache

words = []
path = "Wklej tu scieżkę do swojego pliku ze słówkami!"
count = len(open(path, 'rU').readlines())

for i in range(1,count+1):
    wiersz = linecache.getline(path, i)
    wiersz1 = wiersz.strip()
    words.append(wiersz1)

for i in words:
    url = "http://diki.pl/images-common/en/mp3/" + i +".mp3"
    file_name = url.split('/')[-1]
    u = urllib.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print("Downloading: %s Bytes: %s" % (file_name, file_size))

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print(status)

f.close()