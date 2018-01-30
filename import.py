import re

with open('diki1.txt') as f:
    read_data = f.read()
f.closed

# print(read_data)
wordsEng = list(map(lambda x: x.rstrip(), re.findall("""<span class="hw">\n          (.*?)<""", read_data, re.DOTALL)))
print(wordsEng)
# wordsPl = re.findall("""= \n        (.*?)        <|&nbsp;<span class""", read_data, re.DOTALL);
# wordsPl = list(map(lambda x: x.rstrip(), , read_data, re.DOTALL)))
# print(wordsPl)