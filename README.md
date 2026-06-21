# Physics-Audited Uncertainty Ranking for Perovskite Oxide Screening

A nickelate-inspired case study in reliable materials-informatics workflows.

## Project goal

This project builds a physics-audited machine-learning pipeline for screening perovskite-like oxide materials.

The goal is to predict database-level stability and electronic trends, estimate uncertainty, and rank candidates using physics-based warning flags.

This is a candidate-triage system, not a final discovery oracle.

## What this project does

- Fetches oxide material data from Materials Project.
- Filters strict parent ABO3 candidates.
- Computes physically meaningful descriptors.
- Validates chemical and structural plausibility.
- Trains baseline and graph-based ML models.
- Estimates uncertainty.
- Produces ranked candidate reports with warning flags.

## What this project does not claim

This project does not predict:

- superconductivity,
- Tc,
- exact thin-film synthesis success,
- topotactic reduction kinetics,
- air or moisture stability,
- exact experimental properties.

## Case study

Rare-earth nickelates are used as a case study because their electronic behavior is strongly connected to octahedral distortion and Ni-O-Ni bond geometry.

## Current roadmap

1. Data fetching
2. Composition descriptors
3. Descriptor validation
4. Formula and chemistry filtering
5. Structural descriptors
6. Baseline ML models
7. Graph neural network
8. Uncertainty estimation
9. Candidate ranking
