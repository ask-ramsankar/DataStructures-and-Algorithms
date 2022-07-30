"""
@problem: Graph Problem - Juspay Hiring Challenge
There is a newbie developer A want to clear some doubts with the senior developers in the network.
Only B can clear the doubt's of A. A have to reach B through his follower.

# Input Format:
N no. of Members in Network
member1 member2 member3 . . . memberN
E no. of connections
member1 following member2 -> e1 e2
member2 following member3 -> e2 e3
    .
    .
    .
member u following member v -> eu ev
memberA
memberB

# Output Format
True if A can reach to B else False

# Test Case
## Input
4
2 5 7 9
4
2 7
5 9
7 9
2 5
2
9
## Output
True
"""


class DeveloperNetwork:

    def __init__(self, _members):
        self.__checked_members = dict()
        self.members = dict()
        for _member in _members:
            self.members[_member] = set()

    def __check_connection(self, _member, _target_member):
        """
        This method checks whether the _member is the _target_member.
        Otherwise, It will check the followers of the _members recursively.
        :param _member: current member that we are checking
        :param _target_member: The member who needs to be reached
        :return: Boolean
        """

        # Verify this member already has been checked or not
        if self.__checked_members.get(_member, False):
            return False

        if _member == _target_member:
            return True

        # Marking Checked Members
        # To avoid checking in a loop (eg, a -> b -> c -> a)
        self.__checked_members[_member] = True

        for _follower in self.members[_member]:
            return self.__check_connection(_follower, _target_member)
        return False

    def add_follower(self, _member, _following):
        """
        Adding the connection of a member.
        :param _member: member whose following set needs to be updated
        :param _following: the member who followed by the _member
        :return: None
        """
        self.members[_member].add(_following)

    def reachable(self, _member_a, _member_b):
        """
        It checks the member_a can reach member_b or not using the
        internal __check_connection function.
        :param _member_a:
        :param _member_b:
        :return:
        """
        self.__checked_members = dict()
        return self.__check_connection(_member_a, _member_b)


if __name__ == '__main__':
    total_members = int(input())
    members = list(map(int, input().split(' ')))

    # Creating Network Instance
    network = DeveloperNetwork(members)

    total_connections = int(input())
    for conn_count in range(total_connections):
        network.add_follower(*list(map(int, input().split(' '))))

    member_a = int(input())
    member_b = int(input())

    print(network.reachable(member_a, member_b))
