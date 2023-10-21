
Installation
------------------------------

Within you python enviroment, the package can be simple pip installed:

.. code-block:: python

    pip install pkmodel

However, within a seperate python script the model package can be imported by cloning the package directory and either appending the package using system command and path to directory holding the files:

.. code-block:: python

    import sys
    sys.path.insert(1, 'C:\\path\\to\\directory\\pkmodel') 
    
Or by either copying the pkmodel package to the same directory or to the main python path (for jupyter notebook/spyder this will be main anaconda directory). Packages can then be imported as:

.. code-block:: python

    import pkmodel

Producing Models
------------------------------

The model class holds information regarding a given model, holding the compartments involved, the dosig protocol and solutions. The model is initialise as followed with a given name:  

.. code-block:: python

   # Set first model
   model1 = pk.Model('model1')

Once a model is initialised the class has a function to add a compartment. Compartments require specific names to dictate their function. Compartments include:

* 'central' which is the central/main compartment which other compartments are all linked to
* 'dose' which is a dosing compartment used for subcutaneous dosing protocol
* 'peripheral_N' which is the Nth peripheral compartment which is connected to the central compartment
  
Only one central and one dosing compartment can be given to a single model. Compartments are add using the class' in-built function 'add_compartment'. The function takes:

* name: Compartment type which must be either central, dose, or peripheral_X.
* volume: The volume of compartment, mush be positive and if not set (as not required for dose) it is set to None, which errors if central or peripheral compartment.
* k_rate: Transition rate out of a given compartment. Depending on compartment type is CL, k_a, or Q_Pi.

This is set in the code as follows:

.. code-block:: python

   # Add central compartments  
   model1.add_compartment('central', volume= 1, k_rate=1.0, q0=0)

   # Add peripheral compartments either individually or in bulk
   model1.add_compartment('peripheral_1', k_rate=1.0, q0=0)   
   model1.add_Ncompartments(2, volume= 1, k_rate=1.0, q0=0)
   
   # Add dosing compartment for subcutaneous
   model1.add_compartment('dose', k_rate=1.0, q0=0)

Functions within code then allow you to set given protocol and solve the model.

.. code-block:: python

   # Define protocol
   model1.add_protocol('subcutaneous', dose)

   # Solve model
   model1.solve(t_eval, X )

Using the solution class the model can then be plotted

.. code-block:: python

   # Create solution class 
   solutions = pk.Solution(model1)
   solutions.add_model(model2)

   # Visualise model solutions
   solutions.plot_all()
   solutions.plot_indiv()



