[![Install Dependencies and Run Unit Tests](https://github.com/Software-Engineering-BBSRC-Group-6/PK_modelling/actions/workflows/run-unittests.yml/badge.svg)](https://github.com/Software-Engineering-BBSRC-Group-6/PK_modelling/actions/workflows/run-unittests.yml)
[![Check Systems Compatability](https://github.com/Software-Engineering-BBSRC-Group-6/PK_modelling/actions/workflows/check-systems-compat.yml/badge.svg)](https://github.com/Software-Engineering-BBSRC-Group-6/PK_modelling/actions/workflows/check-systems-compat.yml)
[![codecov](https://codecov.io/gh/Software-Engineering-BBSRC-Group-6/PK_modelling/branch/main/graph/badge.svg?token=gdzMuuonBd)](https://codecov.io/gh/Software-Engineering-BBSRC-Group-6/PK_modelling)


# **Pharmacokinetic Modelling Group Project**
This is a Python package for the analysis PharmacoKinetic (PK) models of an injected solute dynamics over time. The code enables users to create models with custom parameters and find and plot the solutions. Users have the ability to plot multiple models together, and so compare them. Or plot the models separately for a more detailed and specific visualisation of a PK model. View documentation at https://se-pkmodel.readthedocs.io/en/latest/ .

## **Authors**
Joshua Giblin-Burnham, Francesco Rivetti-Macorig, Charlie Hamilton and Christopher Chung


## **Background**

<p align='center'>
  <img width="460" height="300" src = "https://github.com/Joshua-Giblin-Burnham/Software-Engineering/blob/master/docs/images/pk1.jpg">
</p>

  
The field of Pharmacokinetics (PK) provides a quantitative basis for describing the delivery of a drug to a patient, the diffusion of that drug through the plasma/body tissue, and the subsequent clearance of the drug from the patient's system. PK is used to ensure that there is sufficient concentration of the drug to maintain the required efficacy of the drug, while ensuring that the concentration levels remain below the toxic threshold (See Fig 1). Pharmacokinetic (PK) models are often combined with Pharmacodynamic (PD) models, which model the positive effects of the drug, such as the binding of a drug to the biological target, and/or undesirable side effects, to form a full PKPD model of the drug-body interaction. This project will only focus on PK, neglecting the interaction with a PD model.

PK enables the following processes to be quantified:
- Absorption
- Distribution
- Metabolism
- Excretion

These are often referred to as ADME, and taken together describe the drug concentration in the body when medicine is prescribed. These ADME processes are typically described by zeroth-order or first-order rate reactions modelling the dynamics of the quantity of drug **q** , with a given rate parameter **k**, for example:

$$ \frac{dq}{dt} = -k^{*} $$

$$ \frac{dq}{dt} = -kq $$

The body itself is modelled as one or more *compartments*, each of which is defined as a kinetically homogeneous unit (these compartments do not relate to specific organs in the body, unlike Physiologically based pharmacokinetic, PBPK, modeling). There is typically a main *central* compartment into which the drug is administered and from which the drug is excreted from the body, combined with zero or more *peripheral* compartments to which the drug can be distributed to/from the central compartment (See Fig 2). Each peripheral compartment is only connected to the central compartment.

<p align='center'>
  <img width="460" height="300" src = "https://github.com/Joshua-Giblin-Burnham/Software-Engineering/blob/master/docs/images/pk2.jpg">
</p>

The following example PK model describes the two-compartment model shown diagrammatically in Fig 2. The time-dependent variables to be solved are the drug quantity in the central and peripheral compartments, 
*q<sub>c</sub>* and *q<sub>p1</sub>* (units: [ng]) respectively.

$$ \frac{dq}{dt} = Dose(t) - \frac{q_{c}}{V_{c}}CL - Q_{p1} (\frac{q_{c}}{V_{c}} - \frac{q_{p1}}{V_{p1}}), $$

$$ \frac{dq_{p1}}{dt} = Q_{p1} (\frac{q_{c}}{V_{c}} - \frac{q_{p1}}{V_{p1}}) . $$

This model describes an *intravenous bolus* dosing protocol, with a linear clearance from the central compartment (non-linear clearance processes are also possible, but not considered here). The input parameters to the model are:

- The dose function *Dose(t)*, which could consist of instantaneous doses of *X* ng of the drug at one or more time points, or a steady application of *X* ng per hour over a given time period, or some combination.
- V<sub>c</sub> [mL], the volume of the central compartment
- V<sub>p1</sub> [mL], the volume of the first peripheral compartment
- CL [mL/h], the clearance/elimination rate from the central compartment
- Q<sub>p1</sub> [mL/h], the transition rate between central compartment and peripheral compartment 1

Another example model we will show uses subcutaneous dosing, and adds an additional compartment from which the drug is absorbed to the central compartment

$$ \frac{dq_{0}}{dt} = Dose(t) - k_{\alpha}q_{0}, $$

$$ \frac{dq_{c}}{dt} = k_{\alpha}q_{0} - \frac{q_{c}}{V_{c}}CL - Q_{p1} (\frac{q_{c}}{V_{c}} - \frac{q_{p1}}{V_{p1}}), $$

$$ \frac{dq_{p1}}{dt} = Q_{p1} - (\frac{q_{c}}{V_{c}} - \frac{q_{p1}}{V_{p1}}). $$

where *k<sub>α</sub>* [/h] is the “absorption” rate for the s.c dosing.

## For multiple components
When dealing with more complex systems the following equation is used, which builds on the previous equations to enable multi-compartment modeling. 

$$ \frac{dq_{0}}{dt} = Dose(t) - k_{\alpha}q_{0}, $$

$$ \frac{dq_{c}}{dt} = k_{\alpha}q_{0} - \frac{q_{c}}{V_{c}}CL - \sum_{i=1}^{N}Q_{pi} (\frac{q_{c}}{V_{c}} - \frac{q_{pi}}{V_{pi}}) , $$

$$ \frac{dq_{pi}}{dt} = Q_{pi}(\frac{q_{c}}{V_{c}} - \frac{q_{pi}}{V_{pi}}). $$

## **Installation**

Clone the repository to your local machine. Within your python enviroment, the package can be simple pip installed:


    pip install pkmodel

However, within a seperate python script the model package can be imported by cloning the package directory and either appending the package using system command and path to directory holding the files:

    import sys
    sys.path.insert(1, 'C:\\path\\to\\directory\\pkmodel') 
    
Or by either copying the pkmodel package to the same directory or to the main python path (for jupyter notebook/spyder this will be main anaconda directory). Packages can then be imported as:

    import pkmodel

## **Producing Models**

The model class holds information regarding a given model, holding the compartments involved, the dosig protocol and solutions. The model is initialise as followed with a given name:  

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

     # Add central compartments  
     model1.add_compartment('central', volume= 1, k_rate=1.0, q0=0)

     # Add peripheral compartments either individually or in bulk
     model1.add_compartment('peripheral_1', k_rate=1.0, q0=0)   
     model1.add_Ncompartments(2, volume= 1, k_rate=1.0, q0=0)
   
     # Add dosing compartment for subcutaneous
     model1.add_compartment('dose', k_rate=1.0, q0=0)

Functions within code then allow you to set given protocol and solve the model.

     # Define protocol
     model1.add_protocol('subcutaneous', dose)

     # Solve model
     model1.solve(t_eval, X )

Using the solution class the model can then be plotted

     # Create solution class 
     solutions = pk.Solution(model1)
     solutions.add_model(model2)

     # Visualise model solutions
     solutions.plot_all()
     solutions.plot_indiv()