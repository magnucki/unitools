__author__ = 'Rico'

from random import shuffle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("members", help="Number of Members in your group", type=int)
parser.add_argument("groupsize", help="How many people should be in one group",type=int)
parser.add_argument("-e", "--extend", action="store_true",
                    help="extend group single groups if no even solution is possible")
args = parser.parse_args()

group_size = args.groupsize
initial_collection = list(range(1,args.members))
print(initial_collection)
shuffled_teams = []
index = 0
# output_type = len(initial_collection) % group_size
# Rest+1 gibt die Anzahl der gesplitteten Gruppen an.

shuffle(initial_collection)
print(initial_collection)

while(index < len(initial_collection)):
    temp_list = []
    print("index: " + str(index))
    for i in range(0, group_size):
        temp_list.append(initial_collection[index])
        index += 1
    print(temp_list)
    shuffled_teams.append(temp_list)


print(shuffled_teams)