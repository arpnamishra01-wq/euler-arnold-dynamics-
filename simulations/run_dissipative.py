from src.core.dissipative_system import (
    euler_arnold_dissipative
)

from src.core.system import (
    mode_energy,
    total_energy
)

from src.core.parameters import (
    xi0,
    h_case1,
    h_case2,
    gamma,
    t_span,
    t_eval,
    cut
)

from src.core.solver import solve_system

from src.analysis.phase_space_analysis import (
    compare_phase_space
)

from src.analysis.energy_analysis import (
    plot_mode_energies,
    plot_total_energy
)


def solve_dissipative(xi_init, h):

    return solve_system(
        euler_arnold_dissipative,
        xi_init,
        t_span,
        t_eval,
        args=(h, gamma)
    )


sol1 = solve_dissipative(
    xi0,
    h_case1
)

sol2 = solve_dissipative(
    xi0,
    h_case2
)


compare_phase_space(
    sol1,
    sol2,
    cut
)


t = sol2.t

E_modes = mode_energy(sol2)

E_total = total_energy(sol2)


plot_mode_energies(
    t,
    E_modes
)

plot_total_energy(
    t,
    E_total
)
