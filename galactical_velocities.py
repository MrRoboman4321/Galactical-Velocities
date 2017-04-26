import math
from matplotlib import pyplot as plt

#PARAMETERS
RADII_SECTIONS = 50
START_DENSITY = 0
END_DENSITY = 5
G = 6.67408e-11

def velocityByMass(m, r):
	return math.sqrt(G*m/r)

#m = pv
	
def density_basic_glob(r, step): #actually returns the mass inside
	return (4./3*math.pi*(r**3 - (r-step)**3))
	
def density_bulge(r, step): #actually returns the mass inside
	return ((2000*math.e**(-r/2))*(4/3)*(math.pi)*(r**3)) - ((2000*math.e**((-r-step)/-2))*(4/3)*(math.pi)*((r-step)**3))

def density_disk(r, step): #actually returns the mass inside (assuming height of 10 psc)
	return ((780*math.e**(-r/4))*(math.pi)*(r**2)*(10)) - ((780*math.e**((-r-step)/4))*(math.pi)*((r-step)**2)*(10))
	
mass_inside = []
cur_sum = 0

for i in range(RADII_SECTIONS):
	#cur_sum = cur_sum + density_bulge(i, 1) + density_disk(i, 1)
	if(i < END_DENSITY):
		cur_sum += density_basic_glob(i, 1)
		mass_inside.append(cur_sum)
	else:
		mass_inside.append(cur_sum)
		
vals = []

csv = ""
print(mass_inside)
for i in range(len(mass_inside)):
	print(i)
	csv += str(mass_inside[i]) + "," + str(i+1) + "," + str(velocityByMass(mass_inside[i], i+1)) + "\n"
	vals.append([i+1, velocityByMass(mass_inside[i], i+1)])
	
x = [v[0] for v in vals]
y = [v[1] for v in vals]

plt.plot(x, y)
plt.xlabel("Radius (ly)")
plt.ylabel("Velocity (speeds/time)")
plt.title("Galactical Velocities")

plt.show()

file = open("output.csv", "w")
file.write(csv)
file.close()
	
print(mass_inside)
print(len(mass_inside))