import json
from flask import Flask

app = Flask(__name__)


def load_candidates():
    with open("candidates.json", "r", encoding="UTF-8") as file:
        return json.load(file)

@app.route("/")
def get_all():
    data_candidates = ""
    candidates = load_candidates()
    for candidate in candidates:
        data_candidates += f"\n{candidate.get('name')}\n{candidate.get('position')}\n{candidate.get('skills')}\n"
    return f"<pre>{data_candidates}</pre>"

@app.route("/candidates/<pk>")
def get_by_pk(pk):
    data_candidates = ""
    candidates = load_candidates()
    for candidate in candidates:
        if int(pk) == candidate["pk"]:
            return f"<img src='({candidate.get('picture')})'>\n{candidate.get('name')}\n{candidate.get('position')}\n{candidate.get('skills')}\n"
    return "Not found"


@app.route("/skills/<skill_name>")
def get_by_skill(skill_name):
    data_candidates = ""
    candidates = load_candidates()
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower():
            data_candidates += f"<img src='({candidate.get('picture')})'>\n{candidate.get('name')}\n{candidate.get('position')}\n{candidate.get('skills')}\n"
    if data_candidates == "":
        return "Not found"
    else:
        return data_candidates


app.run()


