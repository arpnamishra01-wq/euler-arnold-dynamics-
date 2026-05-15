from scipy.integrate import solve_ivp


def solve_system(system, xi_init, t_span, t_eval, args):

    sol = solve_ivp(
        system,
        t_span,
        xi_init,
        args=args,
        t_eval=t_eval,
        method='DOP853',
        rtol=1e-10,
        atol=1e-10
    )

    return sol
