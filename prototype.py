import pkmodel as pk
import matplotlib.pyplot as plt
import numpy as np

def dose(t, X):
    return X


model1 = pk.Model('model1', Q_p1 = 1.0, V_c = 1.0, V_p1 = 1.0, CL = 1.0, X = 1.0)
model2 = pk.Model('model2', Q_p1 = 2.0, V_c = 1.0, V_p1 = 1.0, CL = 1.0, X = 1.0,  k_a=1.0 )

model1.add_protocols(dose, 'intravenous')
model2.add_protocols(dose, 'subcutaneous')

t_eval, y0 = np.linspace(0, 1, 1000), [np.zeros(2), np.zeros(3)]

fig = plt.figure()
for i, model in enumerate([model1, model2]):

    sol = model.solve(t_eval, y0[i]) 

    plt.plot(sol.t, sol.y[0, :], label=model.name + '- q_c')
    plt.plot(sol.t, sol.y[1, :], label=model.name + '- q_p1')

plt.legend()
plt.ylabel('drug mass [ng]')
plt.xlabel('time [h]')
plt.show()