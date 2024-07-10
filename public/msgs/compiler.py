import os
import json

string = {}
filenames = os.listdir()

for filename in filenames:
  if filename.endswith(".txt"):
    filepath = os.path.join(".", filename)

    with open(filepath, 'r') as f:
      contents = f.read()

      string[filename[:-4]] = {
        "message": contents
      }

print(json.dumps(string, indent=2))