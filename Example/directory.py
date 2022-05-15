#### version 1

from pathlib import Path
x=input('Please input directory:')
entries = Path(x)
for entry in entries.iterdir():
    print(entry.name)





#### version 2
from pathlib import Path

q = input('Please input directory:')
entries = Path(q)
i = []
for entry in entries.iterdir():
    i.append(entry.name)

y=i[1].replace('.mp4', '')
print(y)