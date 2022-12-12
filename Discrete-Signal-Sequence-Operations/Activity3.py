# DSP activity 3 - B.1

# Initial values (for cases: y(n-M))
h = [0,1/2]

print('y(-2) = 0 \n')
print('y(-1) = 1/2 = 0.5 \n')

# Unit step functiom
x = lambda l : 1 if l >= 0 else 0

# Solve 1/2 + 1/2 + (1/4)y(n-2) + y(n-1)
def solveee():
    for n in range(10):

        t = 1 + ((1/4)*h[n+2-2]) + (h[n+2-1])


        # Get fraction form
        mm = ((1/4)*h[n+2-2]).as_integer_ratio()
        nn = (h[n+2-1]).as_integer_ratio()
        j=t.as_integer_ratio()

        # Print iterartions
        print(f'y({n}) =','1/2 + 1/2 +',str(mm[0])+'/'+str(+mm[1]),'+',str(nn[0])+'/'+str(nn[1]))
        print(f'y({n}) =',str(j[0])+'/'+str(+j[1]),'=',t,'\n')

        h.append(t)

solveee()
