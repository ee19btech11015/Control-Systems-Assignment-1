#import necessary libraries
import sympy 
import numpy as np
import matplotlib.pyplot as plt
s,I_1,I_2,V,V_L=sympy.symbols("s I_1 I_2 V V_L") #declare variables
#Mesh Analysis
equation_1=sympy.Eq(((4+ 2/s)*I_1 - (2+1/s)*I_2),V)#Apply KVL around first mesh
equation_2=sympy.Eq(-(2+1/s)*I_1 + (2*s + 1/s + 4)*I_2,0)#Apply KVL around second mesh
solution_12=sympy.solve((equation_1,equation_2),(I_1,I_2)) #solve equations 1 & 2 to find I_1 and I_2
equation_3=sympy.Eq(I_2,solution_12[I_2])#Assign the found out value to I_2
equation_4=sympy.Eq(V_L,2*s*I_2)#voltage across inductor is equal to 2s*I_2
solution_34=sympy.solve((equation_4,equation_3),(V_L,V)) #solve equations 3 and 4 to find V_L and V
G=solution_34[V_L]/solution_34[V] #dividing V_L by V
G=sympy.simplify(G)
print("Transfer Function(G(s))="+str(G))

#plotting transfer function
x=np.linspace(-2,2, 1001)#1001 evenly spaced points on x axis
f = sympy.lambdify(s,G)#function to map from x to y
y=f(x) #array of y values of corresponding x values
plt.plot(x,y)
plt.title("Transfer Function")
plt.xlabel("s")
plt.ylabel("G(s)")
plt.show()