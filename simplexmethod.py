import pulp

# Define the problem
prob = pulp.LpProblem("Pharrell Knives", pulp.LpMaximize)

# Define the decision variables
x1 = pulp.LpVariable("Basic sets", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("Regular sets", lowBound=0, cat='Integer')
x3 = pulp.LpVariable("Deluxe sets", lowBound=0, cat='Integer')

# Define the objective function
profit = 30*x1 + 40*x2 + 60*x3
prob += profit

# Define the constraints
prob += 2*x1 + 2*x2 + 3*x3 <= 800
prob += 1*x1 + 1*x2 + 1*x3 <= 400
prob += 1*x2 + 1*x3 <= 200

# Solve the problem
prob.solve()

# Print the solution
print("Number of basic sets: ", int(pulp.value(x1)))
print("Number of regular sets: ", int(pulp.value(x2)))
print("Number of deluxe sets: ", int(pulp.value(x3)))
print("Maximum profit: ", pulp.value(profit))
