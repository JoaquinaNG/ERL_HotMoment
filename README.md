# About This Repository

This repository complements the conceptual paper that defines hot moments and develops the 4-step hot moment identification framework. It provides a simple, illustrative example of how the framework steps can be implemented in Python.

# Conceptual Overview
### **Hot Moments** are defined as *substantive, quantifiable, and brief deviations in water quality relative to the system's dynamics.*

### 4-Step Hot Moment Identification Framework
i. Temporal Scale Definition — Select the analysis window based on the timescale of the processes and management questions of interest 

ii. R-r Quantification — Compute the magnitude of change (response, R) and the time required to return toward expected, value ranges from the start of the analysis window (recovery, r).

iii. Classification — Classify observations as low/high response and fast/long/no recovery. 
    
iv. Aggregation — Create cohesive events based on the classified observations.

# Repository Structure for Illustrative Example

- **Rr_computation.py**  
  Example functions for calculating response and recovery.

- **SimpleImplemetation_HM.ipynb**  
  Example workflow for calculating and visualizing hot moments.

- **SouthHolland_WaterQualityData_Sept25toJan26.pkl**  
  Water-quality timeseries data used in the example.

- **README.md**  

# Flexibility and Future Development
The framework is intentionally flexible. While the four steps define the way to identify hot moments, there are many ways to achieve the objective of each step. We encourage you to use the most rigorous, data-driven, and mathematically robust analytical and statistical tools available to you at each stage.

We hope these concepts inspire and help you make sense of your data and systems by identifying the **hot moments**!

# Contact and Citation Information
Joaquina Noriega: joaquinanoriegagimenez2027@u.northwestern.edu

This repository is archived on Zenodo:

DOI: https://doi.org/10.5281/zenodo.21797993

If you use this repository or adapt the code for your research, please cite the repository or the associated manuscript, currently under review in Environmental Research Letters, when available.


