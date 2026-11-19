import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x,y,label="Growth",color="blue",marker="o")

plt.xlabel("X Axis Title")
plt.ylabel("Y Axis Title")
plt.title("Simple Line Graph")
plt.legend()

plt.show()