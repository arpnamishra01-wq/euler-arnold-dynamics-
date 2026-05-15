# Energy Transfer and Dissipative Dynamics in a Finite-Dimensional Euler–Arnold System

## Overview

This project presents a numerical investigation of nonlinear energy transfer in a finite-dimensional Euler–Arnold system motivated by geometric mechanics and fluid dynamics.

The system acts as a reduced-order nonlinear model preserving Lie-algebraic interaction structure while remaining computationally tractable. The goal is to study:

- nonlinear mode coupling,
- energy redistribution,
- parameter-sensitive dynamics,
- and the effect of dissipation on long-time evolution.

Both conservative and dissipative simulations are performed to investigate how energy evolves across interacting modes under different parameter regimes.

---

# Physical Motivation

Euler–Arnold equations arise naturally as geodesic flows on Lie groups and appear in geometric mechanics and fluid dynamics.

Unlike exactly solvable rigid-body systems, higher-dimensional Euler–Arnold systems can display:

- nonlinear mode interaction,
- complex phase-space trajectories,
- transient energy redistribution,
- and strong sensitivity to symmetry breaking.

This project studies a six-dimensional truncation inspired by non-compact Lie algebra dynamics, allowing investigation of nonlinear energy transfer in a simplified setting.

---

# Model

The system evolves according to the six-dimensional state vector

$$
x(t) = (x_1,x_2,x_3,x_4,x_5,x_6)
$$

with nonlinear Euler–Arnold dynamics:

$$
\dot{x}_1=(h_2-h_3)x_2x_3+(h_5-h_6)x_5x_6
$$

$$
\dot{x}_2=(h_3-h_1)x_3x_1+(h_6-h_4)x_6x_4
$$

$$
\dot{x}_3=(h_1-h_2)x_1x_2+(h_4-h_5)x_4x_5
$$

$$
\dot{x}_4=(-h_3-h_5)x_3x_5+(h_2+h_6)x_2x_6
$$

$$
\dot{x}_5=(-h_1-h_6)x_1x_6+(h_3+h_4)x_3x_4
$$

$$
\dot{x}_6=(-h_2-h_4)x_2x_4+(h_1+h_5)x_1x_5
$$

where $(h_i$) are constant parameters defining the inertia structure of the system.

---

# Conserved Quantities

In the conservative regime, the Hamiltonian

$$
H=\frac12\sum_{i=1}^{6} h_i x_i^2
$$

is conserved.

The system also possesses Casimir invariants:

$$
C_1=x_1x_4+x_2x_5+x_3x_6
$$

$$
C_2=\frac12(x_1^2+x_2^2+x_3^2-x_4^2-x_5^2-x_6^2)
$$

arising from the Lie–Poisson structure of the dynamics.

These invariants were verified numerically in the conservative regime.

---

# Numerical Implementation

The system was solved numerically using:

- Python
- NumPy
- SciPy (solve_ivp)
- Adaptive Runge–Kutta integrator (DOP853)
- Matplotlib for visualization

Simulation parameters:

- Time interval: $(t \in [0,500]$)
- Relative tolerance: $(10^{-10}$)
- Absolute tolerance: $(10^{-10}$)

---

# Parameter Regimes

Two parameter configurations were studied.

## Weak Asymmetry Regime

$$
h^{(1)}=
(0.966405,\,
0.0567617,\,
0.983445,\,
0.077315,\,
0.915247,\,
0.0762157)
$$

corresponding approximately to $(K \approx 0$).

## Strong Asymmetry Regime

$$
h^{(2)}=
(0.966405,\,
0.0567617,\,
0.983445,\,
0.077315,\,
0.915247,\,
1.85638)
$$

corresponding approximately to $(K \approx 3$).

---

# Initial Conditions

## Trajectory and Dissipative Simulations

$$
x(0)=(-0.499422,\,
0.513364,\,
0.779068,\,
0.844301,\,
-0.127379,\,
0.625175)
$$

## Conservative Energy-Transfer Experiment

$$
x(0)=(3,\,
4,\,
5,\,
10^{-4},\,
10^{-2},\,
1.5)
$$

with parameter set

$$
h=(1,3,6,3,2,10)
$$

---

# Conservative Dynamics

## Phase-Space Structure

Phase-space projections reveal qualitatively different trajectory structures between weak and strong asymmetry regimes.

Even with identical initial conditions, changing the parameter structure significantly modifies the geometry of trajectories, indicating strong sensitivity to nonlinear coupling structure.

The strong asymmetry regime exhibits more complicated trajectory organization and enhanced nonlinear interaction between modes.

---

# Energy Transfer Analysis

To investigate energy redistribution between coupled sectors, the system was partitioned into:

$$
E_A=x_1^2+x_2^2+x_3^2
$$

and

$$
E_B=x_4^2+x_5^2+x_6^2
$$

The individual mode energies are defined as

$$
E_i=\frac12 x_i^2
$$

and the total energy is

$$
E(t)=\frac12\sum_{i=1}^{6}x_i^2
$$

Numerical simulations show:

- oscillatory exchange between the two sectors,
- transient amplification of energy,
- reversible nonlinear transfer,
- and bounded dynamics.

Although transient redistribution is observed, the system does not exhibit sustained directional cascade-like transfer.

---

# Dissipative Extension

To investigate non-conservative dynamics, linear damping was introduced:

$$
\dot{x}_i = F_i(x)-\gamma_i x_i
$$

where $(F_i(x)$) represents the conservative Euler–Arnold dynamics.

The inclusion of dissipation breaks the Hamiltonian structure and introduces energy decay.

---

# Uniform Dissipation

In the first dissipative experiment,

$$
\gamma_i=0.01 \quad \forall i
$$

so all modes are damped equally.

## Observed Behavior

- Total energy decays steadily toward zero.
- Phase-space trajectories contract over time.
- Oscillatory transients persist before eventual suppression.

The system evolves toward a low-energy state due to global damping.

---

# Selective Dissipation

A second numerical experiment introduced damping only in higher-index modes:

$$
\gamma=(0,0,0,0.1,0.1,0.1)
$$

where modes $(4,5,6$) are directly damped while modes $(1,2,3$) remain undamped.

## Observed Behavior

- Modes $(4,5,6$) rapidly lose energy.
- Modes $(1,2,3$) continue persistent oscillatory motion.
- Total energy does not decay completely.
- The system approaches a long-lived oscillatory state with nonzero residual energy.

These simulations demonstrate that the structure of the dissipation operator strongly influences long-time dynamics.

Rather than complete equilibration or thermalization, the system exhibits:

- selective suppression of modes,
- persistent coherent oscillations,
- and survival of undamped energy sectors.

---

# Key Results

The simulations reveal several important qualitative features:

- Strong dependence on parameter asymmetry,
- nonlinear exchange between coupled sectors,
- bounded oscillatory energy transfer,
- contraction of phase-space trajectories under dissipation,
- and persistent residual dynamics under selective damping.

While transient redistribution occurs, the six-dimensional truncation does not exhibit sustained cascade-like behavior characteristic of fully developed turbulent systems.

---

# Figures Included

Representative simulations include:

- Phase-space trajectory comparisons,
- Weak vs strong asymmetry visualizations,
- Energy exchange plots ($(E_A$) and $(E_B$)),
- Total energy decay curves,
- Mode-resolved energy evolution,
- Selective dissipation dynamics,
- Conservative and dissipative trajectory comparisons.

---

# Physical Interpretation

The results suggest that low-dimensional Euler–Arnold truncations can reproduce important structural features of nonlinear dynamics:

- mode interaction,
- transient redistribution,
- parameter-sensitive trajectories,
- and dissipation-induced contraction.

However, the absence of sustained directional cascade indicates that higher-dimensional structure may be required to reproduce genuine turbulent energy transfer.

The selectively damped system further demonstrates that partial dissipation can produce persistent coherent dynamics rather than complete decay.

---

# Future Directions

Possible extensions include:

- larger mode truncations,
- Lyapunov exponent analysis,
- bifurcation studies,
- parameter sweeps,
- chaotic regime characterization,
- and continuum-limit investigations related to turbulence.

---

# Technologies Used

- Python
- NumPy
- SciPy
- Matplotlib

---

# References

- V. I. Arnold — Mathematical Methods of Classical Mechanics
- Euler–Arnold formalism in geometric mechanics
- Lecture notes by Prof. S. G. Rajeev on Lie–Poisson systems and geometric dynamics
