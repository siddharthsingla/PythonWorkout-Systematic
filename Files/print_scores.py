import json
import glob
from collections import defaultdict
def print_scores(dirname):
    print("in fn")
    print(dirname)
    for filename in glob.glob(f'{dirname}/*.json'):
        print(filename)
        output = defaultdict(list)
        with open(filename) as infile:
            data = json.load(infile)
            for line in data:
                for key, value in line.items():
                    output[key].append(value)
        print(f"{filename}")
        for k, v in output.items():
            print(f"\t {k}: min {min(v)}, max {max(v)}")


def print_scoresv2(dirname):
    scores = {}
    for filename in glob.glob(f"{dirname}/*.json"):
        scores[filename] = {}
        with open(filename) as infile:
            for line in json.load(infile):
                for subject, score in line.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)

    for one_class in scores:
        print(one_class)
        for subject, score in scores[one_class].items():
            min_score = min(score)
            max_score = max(score)
            print(subject)
            print(f"\t {min_score}")
            print(f"\t {max_score}")
print_scores("/home/sid/PycharmProjects/PythonWorkout-Systematic/Files/scores")