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

xpoints1 = np.array ([0, 6, 15, 45])
ypoints1 = np.array([0, 250, 30, 150])
xpoints2 = np.array([0, 150, 25, 60])
ypoints2 = np.array([0, 11, 75, 220])

plt.plot(ypoints1, 'o-', mfc='black', mec='black', ms=10)
plt.plot(ypoints2, 'o:r', mfc='r', mec='g', ms = 10)
plt.show()