# 🚀 TOPSIS – Python Package

## Project Description

This package implements **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** using **Python 🐍**.

TOPSIS is a multi-criteria decision-making (MCDM) technique used to rank alternatives based on their distance from an ideal best solution and an ideal worst solution. The alternative closest to the ideal best and farthest from the ideal worst is considered the best option.

This package allows users to perform TOPSIS analysis easily and can be executed directly from the command line after installation.

---

## Package Name

Topsis-Sameer-102303773

---

## Installation

Install the package from PyPI using pip:

pip install Topsis-Sameer-102303773

---

## Usage (Command Line)

Run the TOPSIS method using the following command:

topsis input.csv "1,1,1,2" "+,+,-,+" output.csv

---

## Input File Format

The input file must be in CSV format.

The first column should contain the names of the alternatives.

The remaining columns should contain numeric values only.

A minimum of three columns is required.

Example input file:

Fund Name,P1,P2,P3,P4  
M1,0.67,0.45,6.5,42.6  
M2,0.60,0.36,3.6,53.3  
M3,0.82,0.67,3.8,63.1

---

## Weights and Impacts

Weights represent the importance of each criterion.

Impacts specify whether a criterion is beneficial or non-beneficial.

Use `+` if a higher value is better.

Use `-` if a lower value is better.

The number of weights and impacts must match the number of criteria columns.

---

## Output File Format

The output is a CSV file containing all original columns along with:

Topsis Score – Relative closeness of each alternative to the ideal solution.

Rank – Ranking of alternatives based on the TOPSIS score.

A higher TOPSIS score indicates a better alternative.

---

## Methodology

The TOPSIS algorithm follows these steps:

1. Read the input data from the CSV file
2. Normalize the decision matrix
3. Apply weights to the normalized matrix
4. Determine the ideal best and ideal worst values
5. Calculate the distance from ideal solutions
6. Compute the TOPSIS score
7. Rank the alternatives based on the score

---

## Error Handling

The package handles the following errors:

Incorrect number of command-line arguments  
Input file not found  
Non-numeric values in criteria columns  
Mismatch between number of weights, impacts, and criteria  
Invalid impact values (only + or - allowed)

---

## Dependencies

Python 3.x  
Pandas  
NumPy

---

## Conclusion

This package provides a simple and effective way to perform TOPSIS analysis using Python. It is suitable for academic assignments, projects, and real-world decision-making problems involving multiple criteria.

Happy Decision Making ✨
