import pkmodel as pk
import matplotlib.pyplot as plt
import numpy as np

def dose(t, X):
    return X

X = 1.0
t_eval = np.linspace(0, 1, 1000)

###################################################

model1 = pk.Model('model1')

model1.add_compartment('central', volume= 1, k_rate=1.0)

for i in range(2):
    model1.add_compartment('peripheral_'+str(i), volume= 1, k_rate=1.0)

model1.add_compartment('dose', k_rate=1.0)

model1.add_protocol('subcutaneous', dose)

model1.solve(t_eval, X )

###################################################

model2 = pk.Model('model2')

model2.add_compartment('central',volume= 1.0, k_rate=1.0)
model2.add_compartment('peripheral1', volume= 1.0, k_rate=1.0)

model2.add_protocol('intravenous', dose)

model2.solve(t_eval, X)

###################################################

solutions = pk.Solution(model1)
solutions.add_model(model2)
solutions.plot()
