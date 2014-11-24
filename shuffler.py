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
shuffled_teams = []
index = 0

#checks how many people do not fit in
member_overflow  = len(initial_collection) % group_size

# checks how many full groups are possible
full_groups = len(initial_collection) // group_size

shuffle(initial_collection)

while(index < len(initial_collection)):
    temp_list = []
    for i in range(0, group_size):
        temp_list.append(initial_collection[index])
        index += 1
    print(temp_list)
    # add all groups to a list if needed
    #shuffled_teams.append(temp_list)

# show full list of groups if needed
#print(shuffled_teams)