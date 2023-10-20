# **Pharmacokinetic Modelling Group Project**
A PharmacoKinetic (PK) model for analysis of injected solute dynamics over time.

## **Authors**
Joshua Giblin-Burnham
Francesco Rivetti-Macorig
Charlie Hamilton
Christopher Chung


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
  <img width="460" height="300" src = "https://github.com/Joshua-Giblin-Burnham/Software-Engineering/blob/master/docs/images/pk2.png">
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

## **Installation**

## **Model review**

## **Running Model**
Running model 





