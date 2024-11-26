#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Problem 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the coefficients for the objective function
# Maximize Z = 3A + 4B --> Minimize -3A - 4B
c = [-3, -4]

# Define the coefficients of the inequalities (constraints)
# 2A + 3B <= 12 (Machine time)
# 1A + 2B <= 8 (Raw material)
A = [
    [2, 3],  # Machine time
    [1, 2],  # Raw material
]

b = [12, 8]

# Define the bounds for variables A and B
x0_bounds = (0, None)  # A >= 0
x1_bounds = (0, None)  # B >= 0

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Extract the optimal solution
optimal_A = result.x[0]
optimal_B = result.x[1]
optimal_profit = -result.fun

# Generate data for plotting
x = np.linspace(0, 8, 100)  # A-axis values

# Equations of the constraints
y1 = (12 - 2 * x) / 3  # Machine time constraint
y2 = (8 - x) / 2       # Raw material constraint

# Feasible region boundaries
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r"$2A + 3B \leq 12$", color='blue')
plt.plot(x, y2, label=r"$1A + 2B \leq 8$", color='green')

# Shade the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, color='gray', alpha=0.3, label="Feasible Region")

# Mark the optimal point
plt.scatter(optimal_A, optimal_B, color='red', label=f"Optimal Solution (A={optimal_A:.2f}, B={optimal_B:.2f})")

# Labels and legend
plt.xlabel('Product A')
plt.ylabel('Product B')
plt.title('Maximizing Profit for a Factory')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()

optimal_A, optimal_B, optimal_profit


# In[2]:


# Define the coefficients for the objective function
# Minimize Z = 2X + 5Y
c = [2, 5]

# Define the coefficients of the inequalities (constraints)
# 1X + 2Y <= 6 (Labor)
# 2X + 1Y <= 5 (Material)
A = [
    [1, 2],  # Labor constraint
    [2, 1],  # Material constraint
]
b = [6, 5]

# Define the bounds for variables X and Y
x0_bounds = (0, None)  # X >= 0
x1_bounds = (0, None)  # Y >= 0

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Extract the optimal solution
optimal_X = result.x[0]
optimal_Y = result.x[1]
optimal_cost = result.fun

# Generate data for plotting
x = np.linspace(0, 6, 100)  # X-axis values

# Equations of the constraints
y1 = (6 - x) / 2  # Labor constraint
y2 = (5 - 2 * x)  # Material constraint

# Feasible region boundaries
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r"$1X + 2Y \leq 6$", color='blue')
plt.plot(x, y2, label=r"$2X + 1Y \leq 5$", color='green')

# Shade the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, color='gray', alpha=0.3, label="Feasible Region")

# Mark the optimal point
plt.scatter(optimal_X, optimal_Y, color='red', label=f"Optimal Solution (X={optimal_X:.2f}, Y={optimal_Y:.2f})")

# Labels and legend
plt.xlabel('Product X')
plt.ylabel('Product Y')
plt.title('Minimizing Production Cost for a Manufacturer')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

optimal_X, optimal_Y, optimal_cost



# In[3]:


# Define the coefficients for the objective function
# Maximize Z = 5A + 4B --> Minimize -5A - 4B
c = [-5, -4]

# Define the coefficients of the inequalities (constraints)
# 2A + 1B <= 20 (Labor)
# 3A + 2B <= 30 (Material)
# 1A + 2B <= 18 (Machine time)
A = [
    [2, 1],  # Labor constraint
    [3, 2],  # Material constraint
    [1, 2],  # Machine time constraint
]
b = [20, 30, 18]

# Define the bounds for variables A and B
x0_bounds = (0, None)  # A >= 0
x1_bounds = (0, None)  # B >= 0

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Extract the optimal solution
optimal_A = result.x[0]
optimal_B = result.x[1]
optimal_profit = -result.fun

# Generate data for plotting (only two constraints can be plotted at a time for 2D)
x = np.linspace(0, 20, 100)  # A-axis values

# Equations of the constraints
y1 = (20 - 2 * x)  # Labor constraint
y2 = (30 - 3 * x) / 2  # Material constraint
y3 = (18 - x) / 2  # Machine time constraint

# Feasible region boundaries
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)
y3 = np.clip(y3, 0, None)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r"$2A + 1B \leq 20$", color='blue')
plt.plot(x, y2, label=r"$3A + 2B \leq 30$", color='green')
plt.plot(x, y3, label=r"$1A + 2B \leq 18$", color='orange')

# Shade the feasible region (using the minimum of the constraints)
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), 0, color='gray', alpha=0.3, label="Feasible Region")

# Mark the optimal point
plt.scatter(optimal_A, optimal_B, color='red', label=f"Optimal Solution (A={optimal_A:.2f}, B={optimal_B:.2f})")

# Labels and legend
plt.xlabel('Product A')
plt.ylabel('Product B')
plt.title('Maximizing Production with Multiple Resources')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

optimal_A, optimal_B, optimal_profit


# In[7]:


# Define the coefficients for the objective function
# Maximize Z = 4A + 5B --> Minimize -4A - 5B
c = [-4, -5]

# Define the coefficients of the inequalities (constraints)
# 1A + 2B <= 20 (Advertising budget)
# 1A + 2B <= 15 (Production capacity)
A = [
    [1, 2],  # Advertising budget constraint
    [1, 2],  # Production capacity constraint
]
b = [20, 15]

# Define the bounds for variables A and B
x0_bounds = (0, None)  # A >= 0
x1_bounds = (0, None)  # B >= 0

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Extract the optimal solution
optimal_A = result.x[0]
optimal_B = result.x[1]
optimal_revenue = -result.fun

# Generate data for plotting
x = np.linspace(0, 20, 100)  # A-axis values

# Equations of the constraints
y1 = (20 - x) / 2  # Advertising budget constraint
y2 = (15 - x) / 2  # Production capacity constraint

# Feasible region boundaries
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r"$1A + 2B \leq 20$", color='blue')
plt.plot(x, y2, label=r"$1A + 2B \leq 15$", color='green')

# Shade the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, color='gray', alpha=0.3, label="Feasible Region")

# Mark the optimal point
plt.scatter(optimal_A, optimal_B, color='red', label=f"Optimal Solution (A={optimal_A:.2f}, B={optimal_B:.2f})")

# Labels and legend
plt.xlabel('Product A')
plt.ylabel('Product B')
plt.title('Maximizing Revenue from Sales')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

optimal_A, optimal_B, optimal_revenue


# In[8]:


# Define the coefficients for the objective function
# Maximize Z = 8P1 + 7P2 --> Minimize -8P1 - 7P2
c = [-8, -7]

# Define the coefficients of the inequalities (constraints)
# 3P1 + 4P2 <= 12 (Labor hours)
# 2P1 + 1P2 <= 6 (Capital investment)
A = [
    [3, 4],  # Labor hours constraint
    [2, 1],  # Capital investment constraint
]
b = [12, 6]

# Define the bounds for variables P1 and P2
x0_bounds = (0, None)  # P1 >= 0
x1_bounds = (0, None)  # P2 >= 0

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Extract the optimal solution
optimal_P1 = result.x[0]
optimal_P2 = result.x[1]
optimal_profit = -result.fun

# Generate data for plotting (only two constraints can be plotted at a time for 2D)
x = np.linspace(0, 12, 100)  # P1-axis values

# Equations of the constraints
y1 = (12 - 3 * x) / 4  # Labor hours constraint
y2 = (6 - 2 * x)  # Capital investment constraint

# Feasible region boundaries
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r"$3P1 + 4P2 \leq 12$", color='blue')
plt.plot(x, y2, label=r"$2P1 + 1P2 \leq 6$", color='green')

# Shade the feasible region (using the minimum of the constraints)
plt.fill_between(x, np.minimum(y1, y2), 0, color='gray', alpha=0.3, label="Feasible Region")

# Mark the optimal point
plt.scatter(optimal_P1, optimal_P2, color='red', label=f"Optimal Solution (P1={optimal_P1:.2f}, P2={optimal_P2:.2f})")

# Labels and legend
plt.xlabel('Project P1')
plt.ylabel('Project P2')
plt.title('Resource Allocation for Two Projects')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

optimal_P1, optimal_P2, optimal_profit


# In[9]:


# Define the coefficients for the objective function
# Maximize Z = 5C + 3V --> Minimize -5C - 3V
c = [-5, -3]

# Define the coefficients of the inequalities (constraints)
# 1C + 2V <= 8 (Baking time constraint)
# 3C + 2V <= 12 (Flour constraint)
A = [
    [1, 2],  # Baking time
    [3, 2],  # Flour
]
b = [8, 12]

# Define the bounds for variables C and V
x0_bounds = (0, None)  # C >= 0
x1_bounds = (0, None)  # V >= 0

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Extract the optimal solution
optimal_chocolate = result.x[0]
optimal_vanilla = result.x[1]
optimal_profit = -result.fun

# Generate data for plotting
x = np.linspace(0, 8, 100)  # C-axis values

# Equations of the constraints
y1 = (8 - x) / 2  # Baking time constraint
y2 = (12 - 3 * x) / 2  # Flour constraint

# Feasible region boundaries
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r"$1C + 2V \leq 8$", color='blue')
plt.plot(x, y2, label=r"$3C + 2V \leq 12$", color='green')

# Shade the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, color='gray', alpha=0.3, label="Feasible Region")

# Mark the optimal point
plt.scatter(optimal_chocolate, optimal_vanilla, color='red', label=f"Optimal Solution (C={optimal_chocolate:.2f}, V={optimal_vanilla:.2f})")

# Labels and legend
plt.xlabel('Chocolate Cakes (C)')
plt.ylabel('Vanilla Cakes (V)')
plt.title('Production Planning for a Bakery')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

# Print the optimal solution
optimal_chocolate, optimal_vanilla, optimal_profit


# In[10]:


# Define the coefficients for the objective function
# Minimize Z = 6X + 7Y
c = [6, 7]

# Define the coefficients of the inequalities (constraints)
# 3X + 4Y <= 18 (Fuel hours constraint)
# 2X + 1Y <= 10 (Driver time constraint)
A = [
    [3, 4],  # Fuel hours constraint
    [2, 1],  # Driver time constraint
]
b = [18, 10]

# Define the bounds for variables X and Y
x0_bounds = (0, None)  # X >= 0
x1_bounds = (0, None)  # Y >= 0

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Extract the optimal solution
optimal_X = result.x[0]
optimal_Y = result.x[1]
optimal_cost = result.fun

# Generate data for plotting
x = np.linspace(0, 10, 100)  # X-axis values

# Equations of the constraints
y1 = (18 - 3 * x) / 4  # Fuel hours constraint
y2 = (10 - 2 * x)  # Driver time constraint

# Feasible region boundaries
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r"$3X + 4Y \leq 18$", color='blue')
plt.plot(x, y2, label=r"$2X + 1Y \leq 10$", color='green')

# Shade the feasible region (using the minimum of the constraints)
plt.fill_between(x, np.minimum(y1, y2), 0, color='gray', alpha=0.3, label="Feasible Region")

# Mark the optimal point
plt.scatter(optimal_X, optimal_Y, color='red', label=f"Optimal Solution (X={optimal_X:.2f}, Y={optimal_Y:.2f})")

# Labels and legend
plt.xlabel('Vehicle X')
plt.ylabel('Vehicle Y')
plt.title('Minimizing Cost for a Transport Company')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

# Print the optimal solution
optimal_X, optimal_Y, optimal_cost


# In[11]:


# Define the coefficients for the objective function
# Maximize Z = 10P1 + 12P2 --> Minimize -10P1 - 12P2
c = [-10, -12]

# Define the coefficients of the inequalities (constraints)
# 4P1 + 3P2 <= 30 (Labor hours constraint)
# 1P1 + 2P2 <= 18 (Raw material constraint)
# 3P1 + 2P2 <= 24 (Machine time constraint)
A = [
    [4, 3],  # Labor hours constraint
    [1, 2],  # Raw material constraint
    [3, 2],  # Machine time constraint
]
b = [30, 18, 24]

# Define the bounds for variables P1 and P2
x0_bounds = (0, None)  # P1 >= 0
x1_bounds = (0, None)  # P2 >= 0

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Extract the optimal solution
optimal_P1 = result.x[0]
optimal_P2 = result.x[1]
optimal_revenue = -result.fun

# Generate data for plotting
x = np.linspace(0, 8, 100)  # P1-axis values

# Equations of the constraints
y1 = (30 - 4 * x) / 3  # Labor hours constraint
y2 = (18 - x) / 2  # Raw material constraint
y3 = (24 - 3 * x) / 2  # Machine time constraint

# Feasible region boundaries
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)
y3 = np.clip(y3, 0, None)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r"$4P1 + 3P2 \leq 30$", color='blue')
plt.plot(x, y2, label=r"$1P1 + 2P2 \leq 18$", color='green')
plt.plot(x, y3, label=r"$3P1 + 2P2 \leq 24$", color='orange')

# Shade the feasible region (using the minimum of the constraints)
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), 0, color='gray', alpha=0.3, label="Feasible Region")

# Mark the optimal point
plt.scatter(optimal_P1, optimal_P2, color='red', label=f"Optimal Solution (P1={optimal_P1:.2f}, P2={optimal_P2:.2f})")

# Labels and legend
plt.xlabel('Product P1')
plt.ylabel('Product P2')
plt.title('Maximizing Revenue from Two Products')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

# Print the optimal solution
optimal_P1, optimal_P2, optimal_revenue


# In[15]:


# Define the coefficients for the objective function
# Maximize Z = 500000A + 400000B --> Minimize -500000A - 400000B
c = [-500000, -400000]

# Define the coefficients of the inequalities (constraints)
# 4000A + 3000B <= 5000 (Television budget constraint)
# 2000A + 2500B <= 4500 (Print media budget constraint)
# 1000A + 1500B <= 3000 (Social media budget constraint)
A = [
    [4000, 3000],  # Television budget constraint
    [2000, 2500],  # Print media budget constraint
    [1000, 1500],  # Social media budget constraint
]
b = [5000, 4500, 3000]

# Define the bounds for variables A and B
x0_bounds = (0, None)  # A >= 0
x1_bounds = (0, None)  # B >= 0

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Extract the optimal solution
optimal_A = result.x[0]
optimal_B = result.x[1]
optimal_reach = -result.fun

# Generate data for plotting
x = np.linspace(0, 5, 100)  # A-axis values

# Equations of the constraints
y1 = (5000 - 4000 * x) / 3000  # Television budget constraint
y2 = (4500 - 2000 * x) / 2500  # Print media budget constraint
y3 = (3000 - 1000 * x) / 1500  # Social media budget constraint

# Feasible region boundaries
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)
y3 = np.clip(y3, 0, None)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r"$4000A + 3000B \leq 5000$", color='blue')
plt.plot(x, y2, label=r"$2000A + 2500B \leq 4500$", color='green')
plt.plot(x, y3, label=r"$1000A + 1500B \leq 3000$", color='orange')

# Shade the feasible region (using the minimum of the constraints)
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), 0, color='gray', alpha=0.3, label="Feasible Region")

# Mark the optimal point
plt.scatter(optimal_A, optimal_B, color='red', label=f"Optimal Solution (A={optimal_A:.2f}, B={optimal_B:.2f})")

# Labels and legend
plt.xlabel('Campaign A')
plt.ylabel('Campaign B')
plt.title('Advertising Campaign Budget Allocation')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

# Print the optimal solution
optimal_A, optimal_B, optimal_reach


# In[14]:


# Define the coefficients for the objective function
# Maximize Z = 6A + 5B --> Minimize -6A - 5B
c = [-6, -5]

# Define the coefficients of the inequalities (constraints)
A = [
    [2, 4],  # Meat constraint
    [3, 2],  # Vegetables constraint
    [1, 2],  # Rice constraint
]
b = [30, 24, 20]

# Define the bounds for variables A and B
x0_bounds = (0, None)  # A >= 0
x1_bounds = (0, None)  # B >= 0

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Extract the optimal solution
optimal_A = result.x[0]
optimal_B = result.x[1]
optimal_revenue = -result.fun

# Generate data for plotting
x = np.linspace(0, 8, 100)  # Reduced A-axis values range

# Equations of the constraints
y1 = (30 - 2 * x) / 4  # Meat constraint
y2 = (24 - 3 * x) / 2  # Vegetables constraint
y3 = (20 - x) / 2  # Rice constraint

# Feasible region boundaries
y1 = np.clip(y1, 0, None)
y2 = np.clip(y2, 0, None)
y3 = np.clip(y3, 0, None)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=r"$2A + 4B \leq 30$", color='blue')
plt.plot(x, y2, label=r"$3A + 2B \leq 24$", color='green')
plt.plot(x, y3, label=r"$1A + 2B \leq 20$", color='orange')

# Shade the feasible region (using the minimum of the constraints)
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), 0, color='gray', alpha=0.3, label="Feasible Region")

# Mark the optimal point
plt.scatter(optimal_A, optimal_B, color='red', label=f"Optimal Solution (A={optimal_A:.2f}, B={optimal_B:.2f})")

# Labels and legend
plt.xlabel('Meal A')
plt.ylabel('Meal B')
plt.title('Meal Planning for a School Cafeteria')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

# Print the optimal solution
optimal_A, optimal_B, optimal_revenue


# In[ ]:




