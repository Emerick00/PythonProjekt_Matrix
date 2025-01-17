import numpy as np
from app.utils.checkup_utils import check_is_symmetric, check_positiv_definit


def cholesky_decomposition(in_matrix):
    """
        Berechnet die Cholesky-Zerlegung einer symmetrischen und positiv definiten Matrix.
        Gibt die untere Dreiecksmatrix L zurück, so dass A = L * L.T.
    """

    if not check_is_symmetric(in_matrix):
        raise ValueError("Die angegebene Matrix ist nicht symmetrisch.")

    if not check_positiv_definit(in_matrix) != 'positiv definit':
        raise ValueError("Die angegebene Matrix ist nicht positiv definit.")

    # Anzahl der Zeilen (und Spalten) der quadratischen Matrix
    n = in_matrix.shape[0]

    # Initialisiere L mit Nullen
    L = np.zeros_like(in_matrix)

    for i in range(n):
        for j in range(i + 1):
            _sum = 0

            if j == i:  # Diagonalelemente
                for k in range(j):
                    _sum += L[j, k] ** 2
                L[j, j] = np.sqrt(in_matrix[j, j] - _sum)
            else:
                for k in range(j):
                    _sum += L[i, k] * L[j, k]
                L[i, j] = (in_matrix[i, j] - _sum) / L[j, j]

    return L
