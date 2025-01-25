from coagulation.gillespie import Gillespie
import matplotlib.pyplot as plt

reactions = [
    {
        "reactants": {0: 1, 1: 1},
        "products": {2: 1},
        "rate_constant": 3.2e6,
    },  # r1: x[0] + x[1] -> x[2]
    {
        "reactants": {2: 1},
        "products": {0: 1, 1: 1},
        "rate_constant": 3.1e-3,
    },  # r2: x[2] -> x[0] + x[1]
    {
        "reactants": {0: 1, 3: 1},
        "products": {4: 1},
        "rate_constant": 2.3e7,
    },  # r3: x[0] + x[3] -> x[4]
    {
        "reactants": {4: 1},
        "products": {0: 1, 3: 1},
        "rate_constant": 3.1e-3,
    },  # r4: x[4] -> x[0] + x[3]
    {
        "reactants": {4: 1, 1: 1},
        "products": {3: 1},
        "rate_constant": 4.4e5,
    },  # r5: x[4] + x[1] -> x[3]
    {
        "reactants": {5: 1, 1: 1},
        "products": {3: 1},
        "rate_constant": 1.3e7,
    },  # r6: x[5] + x[1] -> x[3]
    {
        "reactants": {6: 1, 1: 1},
        "products": {3: 1},
        "rate_constant": 2.3e4,
    },  # r7: x[6] + x[1] -> x[3]
    {
        "reactants": {4: 1, 7: 1},
        "products": {8: 1},
        "rate_constant": 2.5e7,
    },  # r8: x[4] + x[7] -> x[8]
    {
        "reactants": {8: 1},
        "products": {4: 1, 7: 1},
        "rate_constant": 1.05,
    },  # r9: x[8] -> x[4] + x[7]
    {
        "reactants": {8: 1},
        "products": {9: 1},
        "rate_constant": 6,
    },  # r10: x[8] -> x[9]
    {
        "reactants": {4: 1, 5: 1},
        "products": {9: 1},
        "rate_constant": 2.2e7,
    },  # r11: x[4] + x[5] -> x[9]
    {
        "reactants": {9: 1},
        "products": {4: 1, 5: 1},
        "rate_constant": 19,
    },  # r12: x[9] -> x[4] + x[5]
    {
        "reactants": {4: 1, 10: 1},
        "products": {11: 1},
        "rate_constant": 1.0e7,
    },  # r13: x[4] + x[10] -> x[11]
    {
        "reactants": {11: 1},
        "products": {4: 1, 10: 1},
        "rate_constant": 2.4,
    },  # r14: x[11] -> x[4] + x[10]
    {
        "reactants": {11: 1},
        "products": {12: 1},
        "rate_constant": 1.8,
    },  # r15: x[11] -> x[12]
    {
        "reactants": {5: 1, 13: 1},
        "products": {6: 1},
        "rate_constant": 7.5e3,
    },  # r16: x[5] + x[13] -> x[6]
    {
        "reactants": {6: 1, 14: 1},
        "products": {15: 1},
        "rate_constant": 2e7,
    },  # r17: x[6] + x[14] -> x[15]
    {
        "reactants": {12: 1, 15: 1},
        "products": {16: 1},
        "rate_constant": 1.0e7,
    },  # r18: x[12] + x[15] -> x[16]
    {
        "reactants": {16: 1},
        "products": {12: 1, 15: 1},
        "rate_constant": 5e-3,
    },  # r19: x[16] -> x[12] + x[15]
    {
        "reactants": {16: 1, 7: 1},
        "products": {17: 1},
        "rate_constant": 1e8,
    },  # r20: x[16] + x[7] -> x[17]
    {
        "reactants": {17: 1},
        "products": {16: 1, 7: 1},
        "rate_constant": 1e-3,
    },  # r21: x[17] -> x[16] + x[7]
    {
        "reactants": {17: 1},
        "products": {18: 1},
        "rate_constant": 8.2,
    },  # r22: x[17] -> x[18]
    {
        "reactants": {15: 1},
        "products": {19: 1},
        "rate_constant": 6e-3,
    },  # r23: x[15] -> x[19]
    {
        "reactants": {18: 1, 19: 1},
        "products": {20: 1},
        "rate_constant": 2.2e4,
    },  # r24: x[18] + x[19] -> x[20]
    {
        "reactants": {17: 1},
        "products": {21: 1},
        "rate_constant": 1e-3,
    },  # r25: x[17] -> x[21]
    {
        "reactants": {6: 1, 20: 1},
        "products": {22: 1},
        "rate_constant": 2e7,
    },  # r26: x[6] + x[20] -> x[22]
    {
        "reactants": {5: 1, 21: 1},
        "products": {23: 1},
        "rate_constant": 4e8,
    },  # r27: x[5] + x[21] -> x[23]
    {
        "reactants": {22: 1},
        "products": {24: 1},
        "rate_constant": 0.2,
    },  # r28: x[22] -> x[24]
    {
        "reactants": {22: 1, 13: 1},
        "products": {25: 1},
        "rate_constant": 1e8,
    },  # r29: x[22] + x[13] -> x[25]
    {
        "reactants": {23: 1},
        "products": {26: 1},
        "rate_constant": 103,
    },  # r30: x[23] -> x[26]
    {
        "reactants": {23: 1},
        "products": {27: 1},
        "rate_constant": 63.5,
    },  # r31: x[23] -> x[27]
    {
        "reactants": {24: 1, 22: 1},
        "products": {28: 1},
        "rate_constant": 1.5e7,
    },  # r32: x[24] + x[22] -> x[28]
    {
        "reactants": {5: 1, 25: 1},
        "products": {26: 1},
        "rate_constant": 9e5,
    },  # r33: x[5] + x[25] -> x[26]
    {
        "reactants": {25: 1},
        "products": {5: 1},
        "rate_constant": 3.6e-4,
    },  # r34: x[25] -> x[5]
    {
        "reactants": {9: 1, 25: 1},
        "products": {27: 1},
        "rate_constant": 3.2e8,
    },  # r35: x[9] + x[25] -> x[27]
    {
        "reactants": {27: 1},
        "products": {9: 1, 25: 1},
        "rate_constant": 1.1e-4,
    },  # r36: x[27] -> x[9] + x[25]
    {
        "reactants": {4: 1, 25: 1},
        "products": {28: 1},
        "rate_constant": 5e7,
    },  # r37: x[4] + x[25] -> x[28]
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

initial_concentrations = [
    25e-12,
    1e-8,
    0,
    1e-10,
    0,
    0,
    0,
    1.6e-7,
    0,
    0,
    9e-8,
    0,
    0,
    1.4e-6,
    0.7e-9,
    0,
    0,
    0,
    0,
    0,
    2e-8,
    0,
    0,
    0,
    0,
    2.5e-9,
    0,
    0,
    3.4e-6,
    0,
    0,
    0,
    0,
    0,
]

if __name__ == "__main__":
    gillespie = Gillespie(
        initial_concentrations=initial_concentrations,
        reactions_with_k=reactions,
        number_of_molecules=1000000,
        max_time=1000,
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