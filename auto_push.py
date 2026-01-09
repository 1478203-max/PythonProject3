#s = "The youngest pope was 11 years old"
#print(s[-11:-1])
#x = s.split()
#print(x[-2] + " " + x[-1] + " " + x[2] + "s")
#print(s.replace("The", "One"))
#print(len(s))
#list= [1, 4]
#print(list.insert(1,9)) # [1, 9, 4]
# Create a list
#numbers = [1, 4]

# Insert 9 at index 1
#numbers.append(2)

# Print the updated list
#print(numbers)
import matplotlib.pyplot as plt
import numpy as np

xpoints1 = np.array ([0, 6])
ypoints1 = np.array([0, 250])
xpoints2 = np.array([0, 150])
ypoints2 = np.array([0, 11])

plt.plot(xpoints1, ypoints1,0)
plt.plot(xpoints2, ypoints2)
plt.show()