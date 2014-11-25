__author__ = 'Rico Magnucki'

from random import shuffle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("members", help="Number of Members in your group", type=int)
parser.add_argument("groupsize", help="How many people should be in one group", type=int)
# parser.add_argument("-e", "--extend", action="store_true",
#                  help="extend group single groups if no even solution is possible")
args = parser.parse_args()

group_size = args.groupsize

# creates list for members
memberlist = list(range(1, args.members + 1))

# number of members
membercount = args.members


def calculate_splitpattern(membercount, groupsize):
    member_overflow = membercount % groupsize
    full_groups = membercount // groupsize

    if (membercount % group_size == 0):
        return [(memberlist // groupsize, groupsize)]
    elif (member_overflow == 1):
        return [(1, groupsize + 1), (full_groups - 1, groupsize)]
    elif (member_overflow == groupsize - 1 ):
        return [(1, member_overflow), (full_groups, groupsize)]
    else:
        return [(1, (groupsize + member_overflow) // 2 ), (1, (groupsize + member_overflow) // 2 + 1),
                (full_groups - 1, groupsize)]


def distribute(splitpattern, list):
    for (x, y) in splitpattern:
        for i in range(x):
            tmp_list = []
            for j in range(y):
                tmp_list.append(list.pop())
            print(tmp_list)


shuffle(memberlist)

distribute(calculate_splitpattern(membercount, group_size), memberlist)
