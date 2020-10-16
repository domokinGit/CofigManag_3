import json
from pathlib import Path

cofig = {}
exec(Path("cofig.py").read_text(), config)
print(json.dumps(cofig["users"], indent = 2))
