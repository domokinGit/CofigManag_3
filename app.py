import json
from pathlib import Path

cofig = {}
exec(Path("cofig.py").read_text(), cofig)
print(json.dumps(cofig["users"], indent=2))
