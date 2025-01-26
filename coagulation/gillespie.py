import numpy as np
import matplotlib.pyplot as plt

initial_concentrations = [
    25e-12,  # TF
    1.0e-8,  # VII
    0.0,  # TF-VII
    1.0e-10,  # VIIa
    0.0,  # TF-VIIa
    0.0,  # Xa
    0.0,  # IIa
    1.6e-7,  # X
    0.0,  # TF-VIIa-X
    0.0,  # TF-VIIa-Xa
    9.0e-8,  # IX
    0.0,  # TF-VIIa-IX
    0.0,  # IXa
    1.4e-6,  # II
    0.7e-9,  # VIII
    0.0,  # VIIIa
    0.0,  # IXa-VIIIa
    0.0,  # IXa-VIIIa-X
    0.0,  # VIIIa1L
    0.0,  # VIIIa2
    2.0e-8,  # V
    0.0,  # Va
    0.0,  # Xa-Va
    0.0,  # Xa-Va-II
    0.0,  # mIIa
    2.5e-9,  # TFPI
    0.0,  # Xa-TFPI
    0.0,  # TF-VIIa-Xa-TFPI
    3.4e-6,  # ATIII
    0.0,  # Xa-ATIII
    0.0,  # mIIa-ATIII
    0.0,  # IXa-ATIII
    0.0,  # IIa-ATIII
    0.0,  # TF-VIIa-ATIII
]

reactions = [
    {
        "reactants": {0: 1, 1: 1},
        "products": {2: 1},
        "rate_constant": 3.1e-3,
    },  # r1: x[0] + x[1] -> x[2]
    {
        "reactants": {2: 1},
        "products": {0: 1, 1: 1},
        "rate_constant": 3.2e6,
    },  # r2: x[2] -> x[0] + x[1]
    {
        "reactants": {0: 1, 3: 1},
        "products": {4: 1},
        "rate_constant": 3.1e-3,
    },  # r3: x[0] + x[3] -> x[4]
    {
        "reactants": {4: 1},
        "products": {0: 1, 3: 1},
        "rate_constant": 2.3e7,
    },  # r4: x[4] -> x[0] + x[3]
    {
        "reactants": {4: 1, 1: 1},
        "products": {4: 1, 3: 1},
        "rate_constant": 4.4e5,
    },  # r5: x[4] + x[1] -> x[4] + x[3]
    {
        "reactants": {5: 1, 1: 1},
        "products": {5: 1, 3: 1},
        "rate_constant": 1.3e7,
    },  # r6: x[5] + x[1] -> x[5] + x[3]
    {
        "reactants": {6: 1, 1: 1},
        "products": {6: 1, 3: 1},
        "rate_constant": 2.3e4,
    },  # r7: x[6] + x[1] -> r[6] + x[3]
    {
        "reactants": {4: 1, 7: 1},
        "products": {8: 1},
        "rate_constant": 1.05,
    },  # r8: x[4] + x[7] -> x[8]
    {
        "reactants": {8: 1},
        "products": {4: 1, 7: 1},
        "rate_constant": 2.5e7,
    },  # r9: x[8] -> x[4] + x[7]
    {
        "reactants": {8: 1},
        "products": {9: 1},
        "rate_constant": 6.0,
    },  # r10: x[8] -> x[9]
    {
        "reactants": {4: 1, 5: 1},
        "products": {9: 1},
        "rate_constant": 19.0,
    },  # r11: x[4] + x[5] -> x[9]
    {
        "reactants": {9: 1},
        "products": {4: 1, 5: 1},
        "rate_constant": 2.2e7,
    },  # r12: x[9] -> x[4] + x[5]
    {
        "reactants": {4: 1, 10: 1},
        "products": {11: 1},
        "rate_constant": 2.4,
    },  # r13: x[4] + x[10] -> x[11]
    {
        "reactants": {11: 1},
        "products": {4: 1, 10: 1},
        "rate_constant": 1.0e7,
    },  # r14: x[11] -> x[4] + x[10]
    {
        "reactants": {11: 1},
        "products": {4: 1, 12: 1},
        "rate_constant": 1.8,
    },  # r15: x[11] -> x[4] + x[12]
    {
        "reactants": {5: 1, 13: 1},
        "products": {5: 1, 6: 1},
        "rate_constant": 7.5e3,
    },  # r16: x[5] + x[13] -> x[5] + x[6]
    {
        "reactants": {6: 1, 14: 1},
        "products": {6: 1, 15: 1},
        "rate_constant": 2.0e7,
    },  # r17: x[6] + x[14] -> x[6] + x[15]
    {
        "reactants": {12: 1, 15: 1},
        "products": {16: 1},
        "rate_constant": 5.0e-3,
    },  # r18: x[12] + x[15] -> x[16]
    {
        "reactants": {16: 1},
        "products": {12: 1, 15: 1},
        "rate_constant": 1.0e7,
    },  # r19: x[16] -> x[12] + x[15]
    {
        "reactants": {16: 1, 7: 1},
        "products": {17: 1},
        "rate_constant": 1.0e-3,
    },  # r20: x[16] + x[7] -> x[17]
    {
        "reactants": {17: 1},
        "products": {16: 1, 7: 1},
        "rate_constant": 1.0e8,
    },  # r21: x[17] -> x[16] + x[7]
    {
        "reactants": {17: 1},
        "products": {5: 1, 16: 1},
        "rate_constant": 8.2,
    },  # r22: x[17] -> x[16] + x[5]
    {
        "reactants": {15: 1},
        "products": {18: 1, 19: 1},
        "rate_constant": 2.2e4,
    },  # r23: x[15] -> x[18] + x[19]
    {
        "reactants": {18: 1, 19: 1},
        "products": {15: 1},
        "rate_constant": 6.0e-3,
    },  # r24: x[18] + x[19] -> x[15]
    {
        "reactants": {17: 1},
        "products": {18: 1, 19: 1, 7: 1, 5: 1},
        "rate_constant": 1.0e-3,
    },  # r25: x[17] -> x[18] + x[19] + x[7] + x[5]
    {
        "reactants": {6: 1, 20: 1},
        "products": {21: 1, 6: 1},
        "rate_constant": 2.0e7,
    },  # r26: x[6] + x[20] -> x[6] + x[21]
    {
        "reactants": {5: 1, 21: 1},
        "products": {22: 1},
        "rate_constant": 0.2,
    },  # r27: x[5] + x[21] -> x[22]
    {
        "reactants": {22: 1},
        "products": {5: 1, 21: 1},
        "rate_constant": 4.0e8,
    },  # r28: x[22] -> x[5] + x[21]
    {
        "reactants": {22: 1, 13: 1},
        "products": {23: 1},
        "rate_constant": 103,
    },  # r29: x[22] + x[13] -> x[23]
    {
        "reactants": {23: 1},
        "products": {22: 1, 13: 1},
        "rate_constant": 1.0e8,
    },  # r30: x[23] -> x[22] + x[13]
    {
        "reactants": {23: 1},
        "products": {24: 1, 22: 1},
        "rate_constant": 63.5,
    },  # r31: x[23] -> x[24] + x[22]
    {
        "reactants": {24: 1, 22: 1},
        "products": {22: 1, 6: 1},
        "rate_constant": 1.5e7,
    },  # r32: x[24] + x[22] -> x[6] + x[22]
    {
        "reactants": {5: 1, 25: 1},
        "products": {26: 1},
        "rate_constant": 3.6e-4,
    },  # r33: x[5] + x[25] -> x[26]
    {
        "reactants": {26: 1},
        "products": {5: 1, 25: 1},
        "rate_constant": 9.0e5,
    },  # r34: x[26] -> x[5] + x[25]
    {
        "reactants": {9: 1, 25: 1},
        "products": {27: 1},
        "rate_constant": 1.1e-4,
    },  # r35: x[9] + x[25] -> x[27]
    {
        "reactants": {27: 1},
        "products": {9: 1, 25: 1},
        "rate_constant": 3.2e8,
    },  # r36: x[27] -> x[9] + x[25]
    {
        "reactants": {4: 1, 26: 1},
        "products": {27: 1},
        "rate_constant": 5.0e7,
    },  # r37: x[4] + x[26] -> x[27]
    {
        "reactants": {5: 1, 28: 1},
        "products": {29: 1},
        "rate_constant": 1.5e3,
    },  # r38: x[5] + x[28] -> x[29]
    {
        "reactants": {24: 1, 28: 1},
        "products": {30: 1},
        "rate_constant": 7.1e3,
    },  # r39: x[24] + x[28] -> x[30]
    {
        "reactants": {12: 1, 28: 1},
        "products": {31: 1},
        "rate_constant": 4.9e2,
    },  # r40: x[12] + x[28] -> x[31]
    {
        "reactants": {6: 1, 28: 1},
        "products": {32: 1},
        "rate_constant": 7.1e3,
    },  # r41: x[6] + x[28] -> x[32]
    {
        "reactants": {4: 1, 28: 1},
        "products": {33: 1},
        "rate_constant": 2.3e2,
    },  # r42: x[4] + x[28] -> x[33]
]


class Gillespie:
    def __init__(
        self, initial_concentrations, reactions_with_k, number_of_molecules, max_time
    ):
        self.number_of_molecules = number_of_molecules
        self.max_time = max_time
        self.initial_concentrations = initial_concentrations
        self.initial_molecules = self.concentrations_to_molecules(
            initial_concentrations
        )
        self.reactions = self.translate_k_to_kappa(reactions_with_k)

    def concentrations_to_molecules(self, concentrations):
        total_concentration = sum(concentrations)

        return [
            round(concentration / total_concentration * self.number_of_molecules)
            for concentration in concentrations
        ]

    def translate_k_to_kappa(self, reactions):
        for reaction in reactions:
            kappa = self.translate_rate_constant(reaction)
            reaction["kappa"] = kappa
        return reactions

    def translate_rate_constant(self, reaction):
        k = reaction["rate_constant"]
        reactants = list(reaction["reactants"].keys())
        num_reactants = len(reactants)  # Total reactant stoichiometry
        if num_reactants == 1:
            # Unimolecular reaction: no adjustment needed
            return k
        elif num_reactants == 2:
            ca0 = self.initial_concentrations[reactants[0]]
            ma0 =  self.initial_molecules[reactants[0]]
            if ma0 == 0: # handle division by 0
                return 0
            return (
                k
                * ca0
                / ma0
            )  # kappa = k * CA0 / MA0
        else:
            raise ValueError(
                "Reactions with more than 2 reactants are not supported in this implementation."
            )

    def calculate_propensities(self, molecules):
        propensities = []
        for reaction in self.reactions:
            propensity = reaction["kappa"]
            for reactant in reaction["reactants"].keys():
                propensity *= molecules[reactant]

            propensities.append(propensity)
        return propensities

    def get_tau(self, a_total):
        chi = np.random.rand()
        return (-np.log(chi) / a_total) / 1000000

    def simulate(self):
        time = 0
        molecules = self.initial_molecules[:]
        times = [time]
        states = [molecules[:]]

        while time < self.max_time:
            propensities = self.calculate_propensities(molecules)
            a_total = sum(propensities)
            if a_total <= 0:
                break

            # Calculate next reaction time
            tau = self.get_tau(a_total)
            time += tau

            # Select reaction
            r = np.random.random() * a_total
            cumulative = 0
            for i, a_i in enumerate(propensities):
                cumulative += a_i
                if r <= cumulative:
                    # Update molecule counts
                    for species, count in reactions[i]["reactants"].items():
                        molecules[species] -= count
                    for species, count in reactions[i]["products"].items():
                        molecules[species] += count
                    break

            # Store results
            times.append(time)
            states.append(molecules[:])

        return times, states


if __name__ == "__main__":
    gillespie = Gillespie(
        initial_concentrations=initial_concentrations,
        reactions_with_k=reactions,
        number_of_molecules=1000000,
        max_time=10000000,
    )
    times, states = gillespie.simulate()
    plt.figure(figsize=(15, 8))
    for i in range(len(gillespie.initial_molecules)):
        if any(state[i] > 0 for state in states):  # Only plot species that change
            plt.plot(times, [state[i] for state in states], label=f"Species {i}")
    plt.xlabel("Time (s)")
    plt.ylabel("Molecule Count")
    plt.title("Blood Coagulation Gillespie Simulation")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()
