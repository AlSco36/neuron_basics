import nengo

model = nengo.Network()

with model:
    a = nengo.Ensemble(70,dimensions=2, radius = 1) #change to sqrt(1^2+1^2)=1.5ish
    
    stim = nengo.Node([0,0])
    nengo.Connection(stim, a)
    
    b = nengo.Ensemble(30,dimensions=1)
    
    def product(x):
        return x[0]*x[1]
        
    nengo.Connection(a, b, function=product)