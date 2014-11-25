__author__ = 'Rico Magnucki'

from random import shuffle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("members", help="Number of Members in your group", type=int)
parser.add_argument("groupsize", help="How many people should be in one group",type=int)
#parser.add_argument("-e", "--extend", action="store_true",
#                  help="extend group single groups if no even solution is possible")
args = parser.parse_args()

group_size = args.groupsize

# creates list for members
memberlist = list(range(1,args.members+1))

# number of members
membercount = args.members



# show full list of groups if needed
#print(shuffled_teams)