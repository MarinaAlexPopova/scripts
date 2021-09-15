import argparse
parser = argparse.ArgumentParser()
parser.add_argument("path", help = 'path to the file')
args = parser.parse_args()
genome_file = args.path
with open(genome_file) as file:
    A_count=0
    for i in file:
        if '>' not in i:
            A_count += i.count('A')
print(A_count)
