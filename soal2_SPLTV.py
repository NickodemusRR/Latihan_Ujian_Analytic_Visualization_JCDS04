# Menyelesaikan SPLTV
# x  - 2y +  z =  6
# 3x +  y - 2z =  4
# 7x - 6y -  z = 10

import numpy as np

# Membuat matriks persamaan
a = np.array([
    [1,-2,1],
    [3,1,-2],
    [7,-6,-1]
])
b = np.array([6,4,10])
c = np.linalg.solve(a,b)

x = round(c[0],1)
y = round(c[1],1)
z = round(c[2],1)

print('X =',c[0])
print('Y =',c[1])
print('Z =',c[2])

# Membuat grafik persamaan
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

plt.figure()

# Persamaan 1 => x  - 2y +  z =  6
x1 = np.array([6, 0, 0])
y1 = np.array([0, -3, 0])
z1 = np.array([[0, 0, 6]])

myplot1 = plt.subplot(131, projection='3d')
myplot1.scatter(x1,y1,z1, c='blue')
myplot1.plot_wireframe(x1, y1, z1, facecolor='red', alpha=.3)
myplot1.set_title('x - 2y + z = 6')
myplot1.set_xlabel('Nilai X')
myplot1.set_ylabel('Nilai Y')
myplot1.set_zlabel('Nilai Z')

# Persamaan 2 => 3x +  y - 2z =  4
x2 = np.array([4/3, 0, 0])
y2 = np.array([0, 4, 0])
z2 = np.array([[0, 0, -2]])

myplot2 = plt.subplot(132, projection='3d')
myplot2.scatter(x2,y2,z2, c='red')
myplot2.plot_wireframe(x2, y2, z2, facecolor='green', alpha=.3)
myplot2.set_title('3x +  y - 2z =  4')
myplot2.set_xlabel('Nilai X')
myplot2.set_ylabel('Nilai Y')
myplot2.set_zlabel('Nilai Z')

# Persamaan 3 => 7x - 6y -  z = 10
x3 = np.array([10/7, 0, 0])
y3 = np.array([0, -10/6, 0])
z3 = np.array([[0, 0, -10]])

myplot3 = plt.subplot(133, projection='3d')
myplot3.scatter(x3,y3,z3, c='violet')
myplot3.plot_wireframe(x3, y3, z3, facecolor='purple', alpha=.3)
myplot3.set_title('7x - 6y -  z = 10')
myplot3.set_xlabel('Nilai X')
myplot3.set_ylabel('Nilai Y')
myplot3.set_zlabel('Nilai Z')

plt.tight_layout()
plt.show()