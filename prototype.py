# Import librarys
import pkmodel as pk
import numpy as np

# Define dosing function
def dose(t, X):
    return X

# Set dose value and time array
X = 1.0
t_eval = np.linspace(0, 1, 1000)

###################################################
# Set first model
model1 = pk.Model('model1')

# Add compartments
model1.add_compartment('central', volume= 1, k_rate=1.0)
model1.add_Ncompartments(1, volume= 1, k_rate=1.0)
model1.add_compartment('dose', k_rate=0.5)

# Define protocol
model1.add_protocol('subcutaneous', dose)

# Solve model
model1.solve(t_eval, X )

###################################################
# Set first model
model2 = pk.Model('model2')

# Add compartments
model2.add_compartment('central',volume= 1.0, k_rate=1.0)
model2.add_compartment('peripheral1', volume= 1.0, k_rate=1.0)

# Define protocol
model2.add_protocol('intravenous', dose)

# Solve model
model2.solve(t_eval, X)

###################################################
# Define model solutions
solutions = pk.Solution(model1)
solutions.add_model(model2)

# Visualise
solutions.plot_all(save = True, fname = 'plot.png')
solutions.plot_indiv(save = True)