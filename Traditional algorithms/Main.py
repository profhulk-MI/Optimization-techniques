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

    def GeneticAlgorithm(self,func,maxrange,minrange,popul_size,no_of_decimals):
        a,b,n=minrange,maxrange,popul_size
        cond=1/10**no_of_decimals
        l=int(2*np.ceil(max([len(np.binary_repr(int(a/cond))),len(np.binary_repr(int(b/cond)))])/2)) # length of chromosomes
        p=a+(b-a)*np.random.random(n)                        #Parents
        while (max(p)-min(p))>cond:
            p_c=[np.binary_repr(int(_/cond),width=l) for _ in p] #Chromosomes of Parents
            fitness=[func(_) for _ in p]
            mod_fit=[max(fitness)+min(fitness)-fitness[_] for _ in range(0,n)]
            angles=[(360*(sum(mod_fit[0:_+1:1]))/sum(mod_fit)) for _ in range(0,n)]
            mating_p=[sum(_>angles) for _ in np.random.random(n)*360]
            mates=np.random.randint(0,n,size=n)
            xOs=[]
            o_c=[]
            o=[]
            for _ in range(0,n):
                xOs.append(int(np.round(np.random.normal(0.5+l/2,0.5,1))))
                while mates[_]==mating_p[_]:
                    mates[_]=(np.random.randint(0,n))
                o_c.append(p_c[mating_p[_]][0:xOs[_]]+p_c[mates[_]][xOs[_]-1:-1])
                o.append(round(int(o_c[_],2)*cond,no_of_decimals))
            print(p)
            p=o
        print(o)
        return o,func(np.mean(o))
