'''
REGRESSION USING LEAST SQUARE METHOD


    X independent
    Y dependent
    Y on X

TAKEAWAYS:
- Model works on increment principal only
- For Accuracy, use more data


IMPROVEMENTS:
- Problem in slope problem fixed
- Able to solve Class problems without much issue
- Can handle decrement values as well
- Needs atleast one or two values to pick on behaviour
- Able to Pick on Trends

    
'''

import numpy as np

def regression ( x , y, val):
    N = 0  # Number of elements
    Sum_y = 0  # Summation of Y elemennts
    Sum_x = 0  # Summation of X elements
    SQ_x = 0  #  Square of X elemets
    SQ_y = 0  # Square of Y elements
    MUL = 0  # Multiplication and sum of X and Y elements


    # Length
    
    N = len(x)
    

    # Sum of y elements
    
    for i in y:
        SQ_y= SQ_y + i**2
        Sum_y = Sum_y + i
        

    # Sum of x elements
    
    for i in x:
        SQ_x = SQ_x + i**2
        Sum_x = Sum_x + i

        

    #Product of x and y
        
    for i in range(0,N):
        MUL = MUL + x[i]*y[i]
        NUMBER = round(MUL,3)


    # Generating eqn using 
    
    L1 = [[N, Sum_x], [Sum_x, SQ_x]]
    L2 = [Sum_y , NUMBER]

    print(L1)
    print(L2)
    

    # Solving Equations

    R = np.linalg.inv(L1).dot(L2)
    Y = R[0] + (R[1]*val)
    print(round(Y,3))
    
    


A = [1,2,3,4,5,6,7,8,9,10]
B = [2,4,6,8,10,12,14,16,18,20]
val = 40

regression( A,B,val)

    
        
