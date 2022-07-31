"""
@problem: Graph Problem - Juspay Hiring Challenge 2
There is a newbie developer A want to clear some doubts with the senior developers in the network.
Only B can clear the doubt's of A. A have to reach B through his followers. In this problem,
we have different delay time for sending message to the different members.
So we have to find the shortest path available from A to B. If connection not found print(-1)

# Input Format:
N no. of Members in Network
member1 member2 member3 . . . memberN
E no. of connections
member1 following member2 message_delay1 -> e1 e2 t1
member2 following member3 message_delay2 -> e2 e3 t2
    .
    .
    .
member u following member v message_delayT -> eu ev tT
memberA
memberB

# Output Format
The shortest time delay if reachable else -1

# Test Case
## Input
4
2 5 7 9
4
2 7 2
5 9 6
7 9 1
2 5 3
2
9
## Output
True
"""


class Connection:

    def __init__(self, _member, _delay):
        self.member = _member
        self.delay = _delay

    def __repr__(self):
        return f'{self.member}: {self.delay}'


class DeveloperNetwork:

    def __init__(self, _members):
        self.__available_time_delays = set()
        self.connections = dict()
        self.message_delays = dict()
        for _member in _members:
            self.connections[_member] = set()

    def __check_connection(self, _member, _target_member, _visited: dict, _message_delay):
        """
        This method checks whether the _member is the _target_member.
        Otherwise, It will check the followers of the _members recursively.
        :param _member: current member that we are checking
        :param _target_member: The member who needs to be reached
        :return: Boolean
        """
        print(_member, _visited)

        if _member == _target_member:
            self.__available_time_delays.add(_message_delay)
            return

        # Verify this member already has been checked or not
        if _visited.get(_member, False):
            return

        # Marking Checked Members
        # To avoid checking in a loop (eg, a -> b -> c -> a)
        _visited[_member] = True

        for _connection in self.connections[_member]:
            self.__check_connection(_connection.member, _target_member, _visited, _message_delay + _connection.delay)

        # Marking the member as not visited to release on returning
        del _visited[_member]

    def add_follower(self, _member, _following, _delay):
        """
        Adding the connection of a member.
        :param _member: member whose following set needs to be updated
        :param _following: the member who followed by the _member
        :param _delay: Message time delay for _member to reach _following member
        :return: None
        """
        self.connections[_member].add(Connection(_following, _delay))

    def reachable(self, _member_a, _member_b):
        """
        It checks the member_a can reach member_b or not using the
        internal __check_connection function.
        :param _member_a: member A
        :param _member_b: member B
        :return:
        """
        self.__available_time_delays = set()
        self.__check_connection(_member_a, _member_b, dict(), 0)
        print(self.__available_time_delays)
        return min(self.__available_time_delays) if self.__available_time_delays else -1


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

    print(network.connections)

    print(network.reachable(member_a, member_b))
