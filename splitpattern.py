__author__ = 'Rico Magnucki'

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("members", help="Number of Members in your group", type=int)
parser.add_argument("groupsize", help="How many people should be in one group", type=int)
args = parser.parse_args()

group_size = args.groupsize
member_list = list(range(0, args.members))
member_overflow =  len(member_list) % group_size
full_groups = len(member_list) // group_size

if (member_overflow == 0):
    print("nothing to do here!")
elif (member_overflow == 1):
    print("One group with {} Members and {} with {}.".format(group_size+1, full_groups-1, group_size))
elif(member_overflow == group_size-1 ):
    print("One group with {} Members and {} with {}.".format(member_overflow, full_groups, group_size))
else:
    if ((group_size+member_overflow) % 2 == 0):
        print("Two groups with {} Members and {} with {}".format((group_size + member_overflow) // 2, full_groups -1, group_size))
    else:
        print("One group with {} members, one with {} and {} with {}.".format((group_size + member_overflow) // 2 ,
                                                                              (group_size + member_overflow) // 2 +1,full_groups-1,group_size))

# TODO Implement this for further usage
#def extend():
#    return
#
#def split():
#    return [[], []]
#
#def stay():
#    return []