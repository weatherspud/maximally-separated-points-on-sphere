Using mathics to compute the derivatives with respect to theta and phi of the distance function of points on the unit sphere:

    In[1]:= x[t_, p_] = Sin[p] Sin[t]
	Out[1]= Sin[p] Sin[t]

	In[2]:= y[t_, p_] = Sin[p] Cos[t]
	Out[2]= Cos[t] Sin[p]

	In[5]:= z[t_, p_] = Cos[p]
	Out[5]= Cos[p]

	In[12]:= distance[t1_, p1_, t2_, p2_] = Sqrt[ ( x[t1, p1] - x[t2, p2] )^2 + ( y[t1, p1] - y[t2, p2] )^2 + ( z[t1, p1] - z[t2, p2] )^2 ]
	Out[12]= Sqrt[(Cos[p1] - Cos[p2]) ^ 2 + (-Cos[t2] Sin[p2] + Cos[t1] Sin[p1]) ^ 2 + (-Sin[p2] Sin[t2] + Sin[p1] Sin[t1]) ^ 2]

	In[17]:= D[distance[t1, p1, t2, p2], t1]
	Out[17]= (-2 (-Cos[t2] Sin[p2] + Cos[t1] Sin[p1]) Sin[p1] Sin[t1] + 2 Cos[t1] (-Sin[p2] Sin[t2] + Sin[p1] Sin[t1]) Sin[p1]) / (2 Sqrt[(Cos[p1] - Cos[p2]) ^ 2 + (-Cos[t2] Sin[p2] + Cos[t1] Sin[p1]) ^ 2 + (-Sin[p2] Sin[t2] + Sin[p1] Sin[t1]) ^ 2])

	In[18]:= D[distance[t1, p1, t2, p2], p1]
	Out[18]= (-2 (Cos[p1] - Cos[p2]) Sin[p1] + 2 Cos[p1] Cos[t1] (-Cos[t2] Sin[p2] + Cos[t1] Sin[p1]) + 2 Cos[p1] (-Sin[p2] Sin[t2] + Sin[p1] Sin[t1]) Sin[t1]) / (2 Sqrt[(Cos[p1] - Cos[p2]) ^ 2 + (-Cos[t2] Sin[p2] + Cos[t1] Sin[p1]) ^ 2 + (-Sin[p2] Sin[t2] + Sin[p1] Sin[t1]) ^ 2])
