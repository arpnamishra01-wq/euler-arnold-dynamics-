import matplotlib.pyplot as plt


def plot_mode_energies(t, E_modes):

    plt.figure(figsize=(10,4))

    for i in range(6):

        plt.plot(
            t,
            E_modes[i],
            linewidth=0.8,
            alpha=0.8,
            label=f"E{i+1}"
        )

    plt.title("Mode Energies")
    plt.xlabel("t")
    plt.ylabel("Energy")

    plt.legend(ncol=3, fontsize=8)

    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.show()


def plot_total_energy(t, E_total):

    plt.figure(figsize=(6,4))

    plt.plot(t, E_total)

    plt.title("Total Energy Decay")

    plt.xlabel("t")

    plt.ylabel("E(t)")

    plt.grid()

    plt.show()
