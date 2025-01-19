import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def LEP_6_coagulation(t, x):
    # Define constants
    k1 = 3.2e6
    k2 = 3.1e-3
    k3 = 2.3e7
    k4 = 3.1e-3
    k5 = 4.4e5
    k6 = 1.3e7
    k7 = 2.3e4
    k8 = 2.5e7
    k9 = 1.05
    k10 = 6
    k11 = 2.2e7
    k12 = 19
    k13 = 1.0e7
    k14 = 2.4
    k15 = 1.8
    k16 = 7.5e3
    k17 = 2e7
    k18 = 1.0e7
    k19 = 5e-3
    k20 = 1e8
    k21 = 1e-3
    k22 = 8.2
    k23 = 6e-3
    k24 = 2.2e4
    k25 = 1e-3
    k26 = 2e7
    k27 = 4e8
    k28 = 0.2
    k29 = 1e8
    k30 = 103
    k31 = 63.5
    k32 = 1.5e7
    k33 = 9e5
    k34 = 3.6e-4
    k35 = 3.2e8
    k36 = 1.1e-4
    k37 = 5e7
    k38 = 1.5e3
    k39 = 7.1e3
    k40 = 4.9e2
    k41 = 7.1e3
    k42 = 2.3e2

    # Reaction rates
    r1 = k1 * x[0] * x[1]
    r2 = k2 * x[2]
    r3 = k3 * x[0] * x[3]
    r4 = k4 * x[4]
    r5 = k5 * x[4] * x[1]
    r6 = k6 * x[5] * x[1]
    r7 = k7 * x[6] * x[1]
    r8 = k8 * x[4] * x[7]
    r9 = k9 * x[8]
    r10 = k10 * x[8]
    r11 = k11 * x[4] * x[5]
    r12 = k12 * x[9]
    r13 = k13 * x[4] * x[10]
    r14 = k14 * x[11]
    r15 = k15 * x[11]
    r16 = k16 * x[5] * x[13]
    r17 = k17 * x[6] * x[14]
    r18 = k18 * x[12] * x[15]
    r19 = k19 * x[16]
    r20 = k20 * x[16] * x[7]
    r21 = k21 * x[17]
    r22 = k22 * x[17]
    r23 = k23 * x[15]
    r24 = k24 * x[18] * x[19]
    r25 = k25 * x[17]
    r26 = k26 * x[6] * x[20]
    r27 = k27 * x[5] * x[21]
    r28 = k28 * x[22]
    r29 = k29 * x[22] * x[13]
    r30 = k30 * x[23]
    r31 = k31 * x[23]
    r32 = k32 * x[24] * x[22]
    r33 = k33 * x[5] * x[25]
    r34 = k34 * x[25]
    r35 = k35 * x[9] * x[25]
    r36 = k36 * x[27]
    r37 = k37 * x[4] * x[25]
    r38 = k38 * x[5] * x[28]
    r39 = k39 * x[24] * x[28]
    r40 = k40 * x[12] * x[28]
    r41 = k41 * x[6] * x[28]
    r42 = k42 * x[4] * x[28]

    # System of ODEs
    xdot = [
        r2 - r1 - r3 + r4,
        r2 - r1 - r6 - r7 - r5,
        r1 - r2,
        -r3 + r4 + r5 + r6 + r7,
        r3 - r4 + r9 - r8 - r11 + r12 - r13 + r14 - r42 - r37 + r15,
        r11 + r12 + r22 - r27 + r28 - r33 + r34 - r38,
        r16 + r32 - r41,
        -r8 + r9 - r20 + r21 + r25,
        r8 - r9 - r10,
        r10 + r11 - r12 - r35 + r36,
        r14 - r13,
        r13 - r14 - r15,
        r15 - r18 + r19 + r25 - r40,
        r30 - r29 - r16,
        -r17,
        r17 - r18 + r19 - r23 + r24,
        -r20 + r21 + r22 + r18 - r19,
        r20 - r21 - r22 - r25,
        r23 - r24 + r25,
        r23 + r25 - r24,
        -r26,
        r26 - r27 + r28,
        r27 - r28 - r29 + r30 + r31,
        r29 - r30 - r31,
        r31 - r32 - r39,
        r34 - r33 - r35 + r36,
        r33 - r34 - r37,
        r35 - r36 + r37,
        -r38 - r39 - r40 - r41 - r42,
        r38,
        r39,
        r40,
        r42,
        r41,
    ]

    return xdot


# Initial conditions
ic = [
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

# Time span
tspan = [0, 700]

# Solve the system using solve_ivp
solution = solve_ivp(
    LEP_6_coagulation, tspan, ic, method="LSODA", t_eval=np.linspace(0, 700, 1000)
)

# Plot results
plt.figure(figsize=(10, 6))
for i in range(len(ic)):
    plt.plot(solution.t, solution.y[i], label=f"x{i+1}")

plt.title("CD Solved Problems - Blood Coagulation")
plt.xlabel("Time (s)")
plt.ylabel("Concentrations")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", ncol=2)
plt.tight_layout()
plt.show()
