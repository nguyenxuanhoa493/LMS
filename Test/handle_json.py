import pandas as pd
import json
import subprocess


INPUT_PATH = "test/input.json"
OUTPUT_PATH = "test/result.xlsx"

with open(INPUT_PATH, "r", encoding="UTF-8") as f:
    data = json.load(f)

result = []
for i in data:
    children = i.get("children", [])
    for c in children:
        temp = {"iid": c["iid"], "id": c["id"], "name": c["name"]}
        result.append(temp)

df = pd.DataFrame(result)
df.to_excel(OUTPUT_PATH, sheet_name="data", index="")
subprocess.run(["start", "excel", OUTPUT_PATH], shell="True", check="")
