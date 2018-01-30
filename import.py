import urllib.request
import re

# urlLogin = "https://www.etutor.pl/account/login"
# https://www.etutor.pl/words/user-words


# html = urllib.request.urlopen(urlLogin).read().decode()
# data = re.findall("""<span class="hw">(.*?)<span class""", opened, re.DOTALL)[-1]


"""
import zipfile, re

f = zipfile.ZipFile("pliki_tekstowe/channel.zip")
num = "90052"
comments = []
while True:
    content = f.read(num + ".txt").decode("utf-8")
    comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
    print(content)
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

print("".join(comments))
"""

with open('diki1.txt') as f:
    read_data = f.read()
f.closed

# print(read_data)
wordsEng = list(map(lambda x: x.rstrip(), re.findall("""<span class="hw">\n          (.*?)<""", read_data, re.DOTALL)))
print(wordsEng)
# wordsPl = re.findall("""= \n        (.*?)        <|&nbsp;<span class""", read_data, re.DOTALL);
# wordsPl = list(map(lambda x: x.rstrip(), , read_data, re.DOTALL)))
# print(wordsPl)