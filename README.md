# **Pharmokinetic Modelling**
The field of Pharmacokinetics (PK) provides a quantitative basis for describing the delivery of a drug to a patient, the diffusion of that drug through the plasma/body tissue, and the subsequent clearance of the drug from the patient's system. PK is used to ensure that there is sufficient concentration of the drug to maintain the required efficacy of the drug, while ensuring that the concentration levels remain below the toxic threshold (See Fig 1). Pharmacokinetic (PK) models are often combined with Pharmacodynamic (PD) models, which model the positive effects of the drug, such as the binding of a drug to the biological target, and/or undesirable side effects, to form a full PKPD model of the drug-body interaction. This project will only focus on PK, neglecting the interaction with a PD model.

PK enables the following processes to be quantified:
- Absorption
- Distribution
- Metabolism
- Excretion

These are often referred to as ADME, and taken together describe the drug concentration in the body when medicine is prescribed. These ADME processes are typically described by zeroth-order or first-order rate reactions modelling the dynamics of the quantity of drug **q** , with a given rate parameter **k**, for example:
$$ \frac{dq}{dt} = -k*, $$
$$ \frac{dq}{dt} = -kq. $$

The body itself is modelled as one or more *compartments*, each of which is defined as a kinetically homogeneous unit (these compartments do not relate to specific organs in the body, unlike Physiologically based pharmacokinetic, PBPK, modeling). There is typically a main *central* compartment into which the drug is administered and from which the drug is excreted from the body, combined with zero or more *peripheral* compartments to which the drug can be distributed to/from the central compartment (See Fig 2). Each peripheral compartment is only connected to the central compartment.

The following example PK model describes the two-compartment model shown diagrammatically in Fig 2. The time-dependent variables to be solved are the drug quantity in the central and peripheral compartments, 
*q<sub>c</sub>* and *q<sub>p1</sub>* (units: [ng]) respectively.
