def bfs(start, end, x_capacity, y_capacity):
    path = []
    front = []
    front.append(start)
	# front = [[0,0]]
    visited = []
    while(front):
        current = front.pop()
		#current = [0,0]
        x = current[0]
        y = current[1]
        path.append(current)
        if x == end or y == end:
            print("The solution to the Water Jug Problem is:")
            return path
	
		# rule 1
        if current[0] < x_capacity and ([x_capacity, current[1]] not in visited):
            front.append([x_capacity, current[1]])
            visited.append([x_capacity, current[1]])

		# rule 2
        if current[1] < y_capacity and ([current[0], y_capacity] not in visited):
            front.append([current[0], y_capacity])
            visited.append([current[0], y_capacity])

		# rule 3
        if current[0] > x_capacity and ([0, current[1]] not in visited):
            front.append([0, current[1]])
            visited.append([0, current[1]])

		# rule 4
        if current[1] > y_capacity and ([x_capacity, 0] not in visited):
            front.append([x_capacity, 0])
            visited.append([x_capacity, 0])

		# rule 5
		#(x, y) -> (min(x + y, x_capacity), max(0, x + y - x_capacity)) if y > 0
        if current[1] > 0 and ([min(x + y, x_capacity), max(0, x + y - x_capacity)] not in visited):
            front.append([min(x + y, x_capacity), max(0, x + y - x_capacity)])
            visited.append([min(x + y, x_capacity), max(0, x + y - x_capacity)])

		# rule 6
		# (x, y) -> (max(0, x + y - y_capacity), min(x + y, y_capacity)) if x > 0
        if current[0] > 0  and ([max(0, x + y - y_capacity), min(x + y, y_capacity)] not in visited):
            front.append([max(0, x + y - y_capacity), min(x + y, y_capacity)])
            visited.append([max(0, x + y - y_capacity), min(x + y, y_capacity)])
        print("Not found")
        return " "

def gcd(a, b):
    if a == 0:
        return b
    return gcd((b%a), (a))
              
if __name__=="__main__":
	x_capacity = float(input("Enter Jug 1 capacity:"))
	y_capacity = float(input("Enter Jug 2 capacity:"))
	end = float(input("Enter target volume:"))

	start = [0, 0] 


	if end % gcd(x_capacity,y_capacity) == 0:
		final_path = bfs(start, end, x_capacity, y_capacity)
		for i in range(0,len(final_path)):
			print(final_path[i])
	else:
		print("No solution possible for this combination.")
