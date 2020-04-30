class direccionCardinal:
    INDEFINIDA = 0
    SUR_A_NORTE = 1
    SUROESTE_A_NORESTE = 2
    OESTE_A_ESTE = 3
    NOROESTE_A_SURESTE = 4
    NORTE_A_SUR = -1
    NORESTE_A_SUROESTE = -2
    ESTE_A_OESTE = -3
    SURESTE_A_NOROESTE = -4

class direccionVectorial:
    DESDE_ACA_HASTA_ALLA = 1
    DESDE_LOS_DOS = 0
    DESDE_ALLA_HASTA_ACA = -1
    INDEFINIDO = None