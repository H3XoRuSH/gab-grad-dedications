import os
import json
import sys

if not os.environ.get('PYTHONHASHSEED'):
    os.environ['PYTHONHASHSEED'] = '69420'
    os.execv(sys.executable, ['python3'] + sys.argv)

string = []
codenames = ''
filenames = os.listdir()

for filename in filenames:
  if filename.endswith(".txt") and filename != "codes.txt":
    filepath = os.path.join(".", filename)

    with open(filepath, 'r') as f:
      name = filename[:-4]
      hashname = str(hash(name))
      contents = f.read()

      string.append({
        "code": hashname,
        "name": name,
        "message": contents
      })

      codenames += f"{name}: {hashname}\n"

with open("msgs.json", "w") as file:
  file.write(json.dumps(string, indent=2))

with open("codes.txt", "w") as file:
  file.write(codenames)
