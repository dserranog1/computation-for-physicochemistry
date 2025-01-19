import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def LEP_6_coagulation(t, x):
    k1 = 3.1e-3
    k2 = 3.2e6
    k3 = 3.1e-3
    k4 = 2.3e7
    k5 = 4.4e5
    k6 = 1.3e7
    k7 = 2.3e4
    k8 = 1.05
    k9 = 2.5e7
    k10 = 6
    k11 = 19
    k12 = 2.2e7
    k13 = 2.4
    k14 = 1.0e7
    k15 = 1.8
    k16 = 7.5e3
    k17 = 2.0e7
    k18 = 5.0e-3
    k19 = 1.0e7
    k20 = 1.0e-3
    k21 = 1.0e8
    k22 = 8.2
    k23 = 2.2e4
    k24 = 6.0e-3
    k25 = 1.0e-3
    k26 = 2.0e7
    k27 = 0.2
    k28 = 4.0e8
    k29 = 103
    k30 = 1.0e8
    k31 = 63.5
    k32 = 1.5e7
    k33 = 3.6e-4
    k34 = 9.0e5
    k35 = 1.1e-4
    k36 = 3.2e8
    k37 = 5.0e7
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
    r34 = k34 * x[26] # difiere
    r35 = k35 * x[9] * x[25]
    r36 = k36 * x[27]
    r37 = k37 * x[4] * x[26] # difiere
    r38 = k38 * x[5] * x[28]
    r39 = k39 * x[24] * x[28]
    r40 = k40 * x[12] * x[28]
    r41 = k41 * x[6] * x[28]
    r42 = k42 * x[4] * x[28]

    # x[0] TF
    # x[1] VII
    # x[2] TF-VII
    # x[3] VIIa
    # x[4] TF-VIIa
    # x[5] Xa
    # x[6] IIa
    # x[7] X
    # x[8] TF-VIIa-X
    # x[9] TF-VIIa-Xa
    # x[10] IX
    # x[11] TF-VIIa-IX
    # x[12] IXa
    # x[13] II
    # x[14] VIII
    # x[15] VIIIa
    # x[16] IXa-VIIIa
    # x[17] IXa-VIIIa-X
    # x[18] VIIIa1L
    # x[19] VIIIa2
    # x[20] V
    # x[21] Va
    # x[22] Xa-Va
    # x[23] Xa-Va-II
    # x[24] mIIa
    # x[25] TFPI
    # x[26] Xa-TFPI
    # x[27] TF-VIIa-Xa-TFPI
    # x[28] ATIII
    # x[29] Xa-ATIII
    # x[30] mIIa-ATIII
    # x[31] IXa-ATIII
    # x[32] IIa-ATIII
    # x[33] TF-VIIa-ATIII

    # System of ODEs
    xdot = [
        r2 - r1 - r3 + r4,  # x[0]: TF
        r2 - r1 - r6 - r7 - r5,  # x[1]: VII
        r1 - r2,  # x[2]: TF-VII
        -r3 + r4 + r5 + r6 + r7,  # x[3]: VIIa
        r3 - r4 + r9 - r8 - r11 + r12 - r13 + r14 - r37 - r42 + r15,  # x[4]: TF-VIIa
        -r11 + r12 + r22 - r27 + r28 - r33 + r34 - r38,  # x[5]: Xa
        r16 + r32 - r41,  # x[6]: IIa
        -r8 + r9 - r20 + r21 + r25,  # x[7]: X
        r8 - r9 - r10,  # x[8]: TF-VIIa-X
        r10 + r11 - r12 - r35 + r36,  # x[9]: TF-VIIa-Xa
        r14 - r13,  # x[10]: IX
        r13 - r14 - r15,  # x[11]: TF-VIIa-IX
        r15 - r18 + r19 + r25 - r40,  # x[12]: IXa
        r30 - r29 - r16,  # x[13]: II
        -r17,  # x[14]: VIII
        r17 - r18 + r19 - r23 + r24,  # x[15]: VIIIa
        -r20 + r21 + r22 + r18 - r19,  # x[16]: IXa-VIIIa
        r20 - r21 - r22 - r25,  # x[17]: IXa-VIIIa-X
        r23 - r24 + r25,  # x[18]: VIIIa1L
        r23 + r25 - r24,  # x[19]: VIIIa2
        -r26,  # x[20]: V
        r26 - r27 + r28,  # x[21]: Va
        r27 - r28 - r29 + r30 + r31,  # x[22]: Xa-Va
        r29 - r30 - r31,  # x[23]: Xa-Va-II
        r31 - r32 - r39,  # x[24]: mIIa
        r34 - r33 - r35 + r36,  # x[25]: TFPI
        r33 - r34 - r37,  # x[26]: Xa-TFPI
        r35 - r36 + r37,  # x[27]: TF-VIIa-Xa-TFPI
        -r38 - r39 - r40 - r41 - r42,  # x[28]: ATIII
        r38,  # x[29]: Xa-ATIII
        r39,  # x[30]: mIIa-ATIII
        r40,  # x[31]: IXa-ATIII
        r42,  # x[32]: IIa-ATIII
        r41,  # x[33]: TF-VIIa-ATIII
    ]

    return xdot


# TF
# VII
# TF-VII
# VIIa
# TF-VIIa
# Xa
# IIa
# X
# TF-VIIa-X
# TF-VIIa-Xa
# IX
# TF-VIIa-IX
# IXa
# II
# VIII
# VIIIa
# IXa-VIIIa
# IXa-VIIIa-X
# VIIIa1L
# VIIIa2
# V
# Va
# Xa-Va
# Xa-Va-II
# mIIa
# TFPI
# Xa-TFPI
# TF-VIIa-Xa-TFPI
# ATIII
# Xa-ATIII
# mIIa-ATIII
# IXa-ATIII
# IIa-ATIII
# TF-VIIa-ATIII

ic = [
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


# Time span
tspan = [0, 700]

# Solve the system using solve_ivp
solution = solve_ivp(
    LEP_6_coagulation, tspan, ic, method="LSODA", t_eval=np.linspace(0, 700)
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
