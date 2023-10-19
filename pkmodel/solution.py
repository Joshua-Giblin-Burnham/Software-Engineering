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
		fig = plt.figure()
		for model in models:
			# how many compartments 
			# for loop again? plot all?
			if model.protocol[-1].name == 'subcutaneous':
				N = len(np.array(model.compartments['peripheral']))+2
			else: 
				N = len(np.array(model.compartments['peripheral']))+1 
			solution = model.solution
			for compartment in range(N):
				plt.plot(solution.t, solution.y[compartment, :], label=f"model_{i+1}")
				# add legend
		

