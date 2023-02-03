"""Create a CSV file, in which each line contains 10 random integers between 10
and 100. Now read the file back, and print the sum and mean of the numbers
on each line."""

import random
import csv
def random_numbers():
    with open("random_numbers.csv", "w") as fin:
        outfile = csv.writer(fin, delimiter= "\t")
        for x in range(20):
            outfile.writerow([random.randint(10, 100) for i in range(10)])
    for line in open("random_numbers.csv"):
        line_sum = sum(int(num) for num in line.split())
        print(f"sum: {line_sum}         mean: {line_sum/len(line.strip().split())}")
random_numbers()