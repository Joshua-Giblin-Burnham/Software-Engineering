#
# Solution class
#
import matplotlib.pylab as plt
import numpy as np

class Solution:
	"""Class to analysis solutions to Pharmokinetic (PK) model that contain defines drug compartments, 
	dosing protocol and holds solutions. 

	Parameters
	----------
	:param models: Model list holding solved models 
	:type models: class"""

	# Initialise class ensuring models variable is 1d list holding models
	def __init__(self, models):
		if isinstance(models, list) == True:
			self.models = models 
		else: 
			self.models = [models]

	def add_model(self, model):
		""" Function to add model to models list.

		Parameters
		----------
		:param models: Model list holding solved models 
		:type models: class
		"""
		# Check if adding list
		if isinstance(model, list) == True:
			self.models += model

		# If single model just append to list
		else: 
			self.models.append(model)
	
	def plot_all(self):
		"""Function to plot all models' results in one graph"""
		# Initialise subplot and set line styles
		fig, ax = plt.subplots(1,1)
		linestyle = ['-.','--']

		# Loop for each model in class list
		for model in self.models:
			# Set number of peripheral compartment in model  
			N = len(np.array(model.compartments['peripheral']))

			# Call model solutions
			solution = model.solution

			# Plot central compartment solution corresponding to first solution
			ax.plot(solution.t, solution.y[0, :], '-', label=model.name+' - q.central')

			# If subcutaneous/ has dosing compartment, plot dose compartment corresponding to last solution
			if model.protocol[-1].name == 'subcutaneous':
				ax.plot(solution.t, solution.y[-1, :], ':', color = plt.gca().lines[-1].get_color(), label=model.name+' - q.dosing')

			# Loop through and plot peripheral compartment solutions
			for n in range(N):
				ax.plot(solution.t, solution.y[n+1, :], ls = np.roll(linestyle, n)[0], 
						color = plt.gca().lines[-1].get_color(), label=model.name+" - q.peripheral_"+str(n+1))
	  
	  	# Set labels and legend
		plt.title('All models')
		ax.set_ylabel('Drug mass (ng)')
		ax.set_xlabel('Time (h)')
		plt.legend()
		plt.show()

	def plot_indiv(self):
		"""Function to plot individual model results"""

		# Loop for each model in class list
		for model in self.models:

			# Initialise subplot and set line styles
			fig, ax = plt.subplots(1,1)
			linestyle = ['-.','--']

			# Set number of peripheral compartment in model  
			N = len(np.array(model.compartments['peripheral']))

			# Call model solutions
			solution = model.solution

			# Plot central compartment solution corresponding to first solution
			ax.plot(solution.t, solution.y[0, :], '-', label = 'Central')

			# If subcutaneous/ has dosing compartment, plot dose compartment corresponding to last solution
			if model.protocol[-1].name == 'subcutaneous':
				ax.plot(solution.t, solution.y[-1, :], ':', color = plt.gca().lines[-1].get_color(), label='Dosing')

			# Loop through and plot peripheral compartment solutions
			for n in range(N):
				ax.plot(solution.t, solution.y[n+1, :], ls = np.roll(linestyle, n)[0], 
						color = plt.gca().lines[-1].get_color(), label = "Peripheral_"+str(n+1))
	  
		  	# Set labels and legend
			plt.title(model.name + ' - ' + model.protocol[-1].name)
			ax.set_ylabel('Drug mass (ng)')
			ax.set_xlabel('Time (h)')
			plt.legend()
			plt.show()

			print(model.protocol[-1].name)

