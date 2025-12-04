import numpy as np 
def convert(T,ppbv):
    result = 600 / (1.380649 * 10**(-23)*T)
    molecules_per_mcube = ppbv * 10**(-9) * result
    x = molecules_per_mcube / 1e6
    print(T,"\n",result,"\n",ppbv,"\n",molecules_per_mcube,"\n",x)
    return(T,result,ppbv,molecules_per_mcube,x)

T = float(input("enter the value of temp in K: "))
ppbv = float(input("enter the volume mixing ration of the ozone: "))


