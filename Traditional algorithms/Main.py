class Optmization1D():

    def SimulatedAnnealing(func,maxrange,minrange):
        a,b=maxrange,minrange
        T=10000000
        x=(a+b)/2
        x_val=[]
        x_val.append(func(x))

        while True:
            val0=func(x)
            x1=float(np.random.normal(x,0.67,1))
            
            if (a<=x1<=b):
                val=sol(x1)
                if val<val0:
                    x_val.append(val)
                    T=T/2
                    x=x1
                    continue
                elif val-val0<0.001 or T<0.0001:
                    break
                else:
                    T=T/2
                    r2=round(float(np.random.random(1)),2)
                    if r2<Boltz((val-val0),T):
                        x=x1
                        x_val.append(val)
                    else: 
                        continue
            else: 
                continue