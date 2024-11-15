import json
# TODO решите задачу
def task() -> float:
    inputfile = "input.json"
    with open(inputfile) as f:
        filedata = json.load(f)
    summa = sum([item["score"] * item["weight"] for item in filedata])
    summa =  round(summa,3)
    return summa
print(task())
