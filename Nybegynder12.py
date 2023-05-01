from cmath import sqrt


a = 5
b = 1
c = 3


d = (a**2) - (4 * b * c) 

print("Diskriminanten er lig " + str(d))

solution1 = (-b + sqrt(d))/2*a
solution2 = (-b - sqrt(d))/2*a
print("Resultaterne er lig " + str(solution1) + " og " + str(solution2))
xkoord = -b / 2*a
ykoord = -d / 4*a
print("Toppunktet ligger på x-koordinatet: " + str(xkoord) + " og y-koordinatet: " + str(ykoord))