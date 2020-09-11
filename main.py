from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

f = open("E:\\wuli\\model\\model_damit_polished_A106.txt", 'r')
data = f.read()
data = data.splitlines()
nfac = int(data[0].split()[0])
nedge = int(data[0].split()[1])
xyz = []
n = []
for l in range(1, nfac + 1):
    xyz.append([float(data[l].split()[0]), float(data[l].split()[1]), float(data[l].split()[2])])

for l in range(nfac + 1, nfac + nedge + 1):
    n.append([int(data[l].split()[0]), int(data[l].split()[1]), int(data[l].split()[2])])

for i in range(nedge):
    x = []
    y = []
    z = []
    for j in range(3):
        x.append(xyz[n[i][j] - 1][0])
        y.append(xyz[n[i][j] - 1][1])
        z.append(xyz[n[i][j] - 1][2])
    ax.plot3D(x, y, z)

plt.show()
