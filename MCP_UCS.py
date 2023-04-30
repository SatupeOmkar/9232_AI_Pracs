from queue import PriorityQueue

print("--- Missionaries Cannibals Problem Using Uniform Cost Search ----")
print("\n")

m = int(input("Enter the number of missionaries:"))
c = int(input("Enter the number of cannibals:"))
b = int(input("Enter the side of the river where the boat is present(0 for left, 1 for right):"))
print("\n")
print("--- Solution ---\n")

# define the initial state
initial_state = (m, c, b)

# define the goal state
goal_state = (0, 0, 0)

# define the set of valid actions
actions = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]

# define the cost function
def cost(state, action):
    # define the cost of each action based on the distance between states and the resources used
    if action == (1, 0) or action == (0, 1):
        # moving one missionary or cannibal
        return 1
    elif action == (2, 0) or action == (0, 2):
        # moving two missionaries or cannibals
        return 2
    elif action == (1, 1):
        # moving one missionary and one cannibal
        return 3
    # return infinity for invalid actions
    return float('inf')

# define the search function
def search():
    # initialize the priority queue with the initial state and its cost
    frontier = PriorityQueue()
    frontier.put((0, initial_state, []))
    # initialize the explored set
    explored = set()
    # loop until the goal state is found or the frontier is empty
    while not frontier.empty():
        # get the state with the lowest cost
        _, current_state, path = frontier.get()
        # check if the current state is the goal state
        if current_state == goal_state:
            return path
        # add the current state to the explored set
        explored.add(current_state)
        # generate the successor states and their paths
        for action in actions:
            # check if the action is valid
            if current_state[2] == 1 and (current_state[0] - action[0] < current_state[1] - action[1] or
                                         current_state[0] - action[0] < 0 or
                                         current_state[1] - action[1] < 0):
                continue
            elif current_state[2] == 0 and ((current_state[0] + action[0] < current_state[1] + action[1] and
                                              current_state[0] + action[0] != 0) or
                                             current_state[0] + action[0] > 3 or
                                             current_state[1] + action[1] > 3):
                continue
            # generate the successor state and its path
            if current_state[2] == 1:
                successor_state = (current_state[0] - action[0], current_state[1] - action[1], 0)
            else:
                successor_state = (current_state[0] + action[0], current_state[1] + action[1], 1)
            successor_path = path + [(current_state, action, successor_state)]
            # check if the successor state has already been explored
            if successor_state in explored:
                continue
            # calculate the cost of the successor state and its path
            successor_cost = sum(cost(successor_path[i][2], successor_path[i][1]) for i in range(len(successor_path)))
            # add the successor state and its path to the priority queue
            frontier.put((successor_cost, successor_state, successor_path))
    # if the goal state is not found, return None
    return None

# run the search function and print the result
result = search()
if result is not None:
    total_cost = 0
    for i, step in enumerate(result):
        cost = step[1][0] + step[1][1]
        total_cost += cost
        print("Step", i+1, ":")
        print(" ", step[0], "->", step[1], "->", step[2], "Cost:", cost)
    print("Total cost:", total_cost)
else:
    print("No solution found.")