import pkmodel as pk
import matplotlib.pyplot as plt
import numpy as np

def dose(t, X):
    return X

X = 1.0

###################################################
model1 = pk.Model('model1')

model1.add_compartment('central', volume= 1, k_rate=1.0)

for i in range(2):
    model1.add_compartment('peripheral_'+str(i), volume= 1, k_rate=1.0)

model1.add_compartment('dose', k_rate=1.0)

model1.add_protocol('subcutaneous', dose)

###################################################

model2 = pk.Model('model2')

model2.add_compartment('central',volume= 1.0, k_rate=1.0)
model2.add_compartment('peripheral1', volume= 1.0, k_rate=1.0)

model2.add_protocol('intravenous', dose)

###################################################

t_eval, q0 = np.linspace(0, 1, 1000), [np.zeros(4), np.zeros(2)]

m1_solution = model1.solve(t_eval, q0[0], X)
m2_solution = model2.solve(t_eval, q0[1], X)

