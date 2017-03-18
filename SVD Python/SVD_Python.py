import csv
import numpy as np
with open('linSys.csv', 'r') as file:
	reader = csv.reader(file)
	x = list(reader)
i = 0
while i < len(x):
	x[i].pop()
	i += 1

print(x)
#input = csv.reader(open("linSys.csv", "rt"), delimiter = ",")
#print(input)d
#x = list(input)

#while i < len(x):
#	x[i].pop()
#	i++

array = np.array(x).astype("double")
#print(array)
matrix = np.matrix(array)
##print(matrix)
U, s, V = np.linalg.svd(matrix, full_matrices=True)
print("U = ", U)
print("s = ", s)
print("V = ", V)
np.savetxt("U.csv", U, delimiter = ',')
np.savetxt("s.csv", s, delimiter = ',')
np.savetxt("V.csv", V, delimiter = ',')