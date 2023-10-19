#
# Solution class
#
import matplotlib.pylab as plt
import numpy as np

class Solution:
	"""A Pharmokinetic (PK) model solution

	Parameters
	----------

	value: numeric, optional
		an example paramter

	"""
	def __init__(self, models):
		if isinstance(models, list) == True:
			self.models = models 
		else: 
			self.models = [models]

	def plot(self):
		fig, ax = plt.subplots(1,1)
		linestyle = ['-.','--']

		for model in self.models:
			# how many compartments 
			# for loop again? plot all?
			solution = model.solution

			ax.plot(solution.t, solution.y[0, :], '-', label=model.name+' - q.central')
				
			if model.protocol[-1].name == 'subcutaneous':
				ax.plot(solution.t, solution.y[-1, :], ':', color = plt.gca().lines[-1].get_color(), label=model.name+'q.dosing')

			N = len(np.array(model.compartments['peripheral']))

			for compartment in range(N):
				ax.plot(solution.t, solution.y[compartment+1, :], ls = np.roll(linestyle, compartment)[0], color = plt.gca().lines[-1].get_color(), label=model.name+"q.peripheral_"+str(compartment+1))


		plt.legend()
		plt.show()
		# add legend and shit
