import matplotlib.pyplot as plt
import numpy as np

def box_1_belasting(bruto_inkomen):
    schijf_1_inkomen = min((73031.0, bruto_inkomen))
    schijf_2_inkomen = max((0, bruto_inkomen - schijf_1_inkomen))
    
    return schijf_1_inkomen*0.3693 + schijf_2_inkomen*0.4950

def algemeneheffingskorting(bruto_inkomen):
    if bruto_inkomen < 22661:
        return 3070
    elif bruto_inkomen < 73031:
        return 3070 - 0.06095*(bruto_inkomen - 22660)
    else:
        return 0

def arbeidsheffingskorting(bruto_inkomen):
    if bruto_inkomen < 10741:
        return 0.08231*(bruto_inkomen)
    elif bruto_inkomen < 23201:
        return 884 + 0.029861*(bruto_inkomen - 10740)
    elif bruto_inkomen < 37691:
        return 4605 + 0.03085*(bruto_inkomen - 23201)
    elif bruto_inkomen < 115295:
        return 5052 - 0.06510*(bruto_inkomen - 37691)
    else:
        return 0
    
# zorgtoeslag
def zorgtoeslag_maandelijks(bruto_inkomen):
    toetsingsinkomens = [27000, 27500, 28000, 28500, 29000, 29500, 30000, 30500, 31000, 31500, 32000, 32500, 33000, 33500, 34000, 34500, 35000, 35500, 36000, 36500, 37000, 37496, float('inf')]
    bedrag_per_maand = [123, 121, 115, 110, 104, 98, 93, 87, 81, 75, 70, 64, 58, 53, 47, 41, 36, 30, 24, 19, 13, 7, 0]
    schaal_index = 0
    while toetsingsinkomens[schaal_index] <= bruto_inkomen:
        schaal_index = schaal_index + 1

    return bedrag_per_maand[schaal_index]

def zorgtoeslag_jaarlijks(bruto_inkomen):
    return 12*zorgtoeslag_maandelijks(bruto_inkomen)

# huurtoeslag
    
# kinderopvangtoeslag
    
# kindgebonden budget

## ------------------ Main method ---------------------
if __name__ == '__main__':
    bruto_inkomens = np.arange(2e4, 8e4, 10)
    netto_inkomens = np.zeros(bruto_inkomens.shape)
    toeslagen_inkomens = np.zeros(bruto_inkomens.shape)

    for i, bruto_inkomen in enumerate(bruto_inkomens):
        heffing = box_1_belasting(bruto_inkomen)
        heffingskorting = arbeidsheffingskorting(bruto_inkomen) + algemeneheffingskorting(bruto_inkomen)
        netto_inkomen = bruto_inkomen - max((0, heffing - heffingskorting))
        netto_inkomens[i] = netto_inkomen

        toeslagen_totaal = zorgtoeslag_jaarlijks(bruto_inkomen)
        toeslagen_inkomen = netto_inkomen + toeslagen_totaal
        toeslagen_inkomens[i] = toeslagen_inkomen

    plt.plot(bruto_inkomens, bruto_inkomens, label="geen belasting")
    plt.plot(bruto_inkomens, netto_inkomens, label="belasting")
    plt.plot(bruto_inkomens, toeslagen_inkomens, label="toeslagen")
    plt.xlabel("bruto"); plt.ylabel("netto")
    plt.grid(); plt.legend(); plt.show()