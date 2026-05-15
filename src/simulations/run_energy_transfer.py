import numpy as np
import matplotlib.pyplot as plt

from src.core.system import euler_arnold
from src.core.solver import solve_system


# Parameters for energy-transfer experiment
h = [1, 3, 6, 3, 2, 10]


# Initial condition:
# energy concentrated mostly in first three modes
xi0 = [
    3.0,
    4.0,
    5.0,
    0.0001,
    0.01,
    1.5
]


# Time settings
t_span = (0, 100)

t_eval = np.linspace(0, 100, 10000)


# Solve system
sol = solve_system(
    euler_arnold,
    xi0,
    t_span,
    t_eval,
    args=(h,)
)


# Extract modes
x1, x2, x3, x4, x5, x6 = sol.y


# Compute grouped energies
EA = x1**2 + x2**2 + x3**2

EB = x4**2 + x5**2 + x6**2


# Plot
plt.figure(figsize=(7,5))

plt.plot(
    sol.t,
    EA,
    label="E_A"
)

plt.plot(
    sol.t,
    EB,
    label="E_B"
)

plt.xlabel("Time")

plt.ylabel("Energy")

plt.title("Energy Transfer Between Modes")

plt.legend()

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "energy_transfer.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
