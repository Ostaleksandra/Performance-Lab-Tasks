import json
import sys

values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]

with open(values_file, encoding="utf-8") as f:
    values = json.load(f)

dict_values = {}
for item in values["values"]:
    dict_values[item["id"]] = item["value"]

with open(tests_file, encoding="utf-8") as f:
    tests = json.load(f)

def report(items):
    for item in items:
        if item["id"] in dict_values:
            item["value"] = dict_values[item["id"]]

        if "values" in item:
            report(item["values"])

report(tests["tests"])

with open(report_file, 'w', encoding="utf-8") as f:
    json.dump(tests, f, indent=2)
