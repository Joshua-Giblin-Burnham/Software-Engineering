Basic  Model
-----------------------------------

These are often referred to as ADME, and taken together describe the drug concentration in the body when medicine is 
prescribed. These ADME processes are typically described by zeroth-order or first-order rate reactions modelling the 
dynamics of the quantity of drug **q** , with a given rate parameter **k**, for example:

.. math:: \frac{dq}{dt} = -k^{*} 

.. math:: \frac{dq}{dt} = -kq 

The body itself is modelled as one or more *compartments*, each of which is defined as a kinetically homogeneous unit 
(these compartments do not relate to specific organs in the body, unlike Physiologically based pharmacokinetic, PBPK, 
modeling). There is typically a main *central* compartment into which the drug is administered and from which the drug 
is excreted from the body, combined with zero or more *peripheral* compartments to which the drug can be distributed 
to/from the central compartment (See Fig 2). Each peripheral compartment is only connected to the central compartment.

.. image:: images/pk2.svg


Two Compartment Model
-----------------------------------

The following example PK model describes the two-compartment model shown diagrammatically in Fig 2. The time-dependent 
variables to be solved are the drug quantity in the central and peripheral compartments, *q<sub>c</sub>* and 
*q<sub>p1</sub>* (units: [ng]) respectively.

.. math:: \frac{dq}{dt} = Dose(t) - \frac{q_{c}}{V_{c}}CL - Q_{p1} (\frac{q_{c}}{V_{c}} - \frac{q_{p1}}{V_{p1}}), 

.. math:: \frac{dq_{p1}}{dt} = Q_{p1} (\frac{q_{c}}{V_{c}} - \frac{q_{p1}}{V_{p1}}) . 

This model describes an *intravenous bolus* dosing protocol, with a linear clearance from the central compartment (non-linear clearance processes are also possible, but not considered here). The input parameters to the model are:

- The dose function *Dose(t)*, which could consist of instantaneous doses of *X* ng of the drug at one or more time points, or a steady application of *X* ng per hour over a given time period, or some combination.
- V<sub>c</sub> [mL], the volume of the central compartment
- V<sub>p1</sub> [mL], the volume of the first peripheral compartment
- CL [mL/h], the clearance/elimination rate from the central compartment
- Q<sub>p1</sub> [mL/h], the transition rate between central compartment and peripheral compartment 1


Subcutaneous Model
-----------------------------------

Another example model we will show uses subcutaneous dosing, and adds an additional compartment from which the drug is 
absorbed to the central compartment

.. math:: \frac{dq_{0}}{dt} = Dose(t) - k_{\alpha}q_{0}, 

.. math:: \frac{dq_{c}}{dt} = k_{\alpha}q_{0} - \frac{q_{c}}{V_{c}}CL - Q_{p1} (\frac{q_{c}}{V_{c}} - \frac{q_{p1}}{V_{p1}}), 

.. math:: \frac{dq_{p1}}{dt} = Q_{p1} - (\frac{q_{c}}{V_{c}} - \frac{q_{p1}}{V_{p1}}). 

where 
.. math:: *k<sub>α</sub>* [/h] 
is the “absorption” rate for the s.c dosing.


N Compartment Model
-----------------------------------

When dealing with more complex systems the following equation is used, which builds on the previous equations to enable multi-compartment modeling. 

.. math:: \frac{dq_{0}}{dt} = Dose(t) - k_{\alpha}q_{0}, 

.. math:: \frac{dq_{c}}{dt} = k_{\alpha}q_{0} - \frac{q_{c}}{V_{c}}CL - \sum_{i=1}^{N}Q_{pi} (\frac{q_{c}}{V_{c}} - \frac{q_{pi}}{V_{pi}}) , 

.. math:: \frac{dq_{pi}}{dt} = Q_{pi}(\frac{q_{c}}{V_{c}} - \frac{q_{pi}}{V_{pi}}). 

