import matplotlib.pyplot as plt

# Data
with open("linear_regression_data.txt", "r") as file:
    data = file.readlines()

data = [float(i) for i in data]
print(data)

# Plot
plt.plot(data)
plt.title("Linear Regression Cost")
plt.xlabel("Epoch")
plt.ylabel("Cost")
plt.show()