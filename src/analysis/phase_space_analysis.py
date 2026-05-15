import matplotlib.pyplot as plt
import numpy as np


def plot_dense_projection(
    solve_system_function,
    h,
    start
):

    plt.figure(figsize=(6,6))

    for _ in range(3):

        xi_rand = np.random.uniform(-1, 1, 6)

        sol = solve_system_function(xi_rand, h)

        plt.plot(
            sol.y[0][start:],
            sol.y[3][start:],
            linewidth=0.2
        )

    plt.xlabel("xi1")
    plt.ylabel("xi4")

    plt.axis('equal')

    plt.tight_layout()

    plt.show()


def compare_phase_space(
    sol1,
    sol2,
    cut
):

    pairs = [(0,3), (4,5), (2,5)]

    labels = [
        "x1 vs x4",
        "x5 vs x6",
        "x3 vs x6"
    ]

    fig, ax = plt.subplots(2, 3, figsize=(13, 7))

    for row, sol in enumerate([sol1, sol2]):

        for col, (a, b) in enumerate(pairs):

            ax[row, col].plot(
                sol.y[a][cut:],
                sol.y[b][cut:],
                linewidth=0.6
            )

            ax[row, col].set_xlabel(f"x{a+1}")
            ax[row, col].set_ylabel(f"x{b+1}")

            title = "K ≈ 0 " if row == 0 else "K ≈ 3 "

            ax[row, col].set_title(
                f"{title}\n{labels[col]}"
            )

            ax[row, col].axis("equal")

            ax[row, col].grid(alpha=0.3)

    plt.tight_layout()

    plt.savefig(
        "phase_space_atlas.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
