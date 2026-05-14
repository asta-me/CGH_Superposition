"""
Algoritmo generico di sovrapposizione basato sul metodo Weighted Gerchberg-Saxton (WGS).

Questo script implementa una sintesi olografica iterativa phase-only, in cui ogni
contributo target e rappresentato da una base di fase in phase_stack.
La stessa formulazione puo essere usata per:
- array di punti (trap ottiche),
- linee,
- pattern di intensita 2D arbitrari,
purche sia fornito il corrispondente insieme di maschere di fase base.

Il vettore opzionale desired_weights permette un'allocazione di potenza non uniforme.
"""

import numpy as np

def wgs_traps(phase_stack, iters, desired_weights=None):
    """
    Weighted Gerchberg-Saxton optimization with optional non-uniform target intensities.

    Parameters:
    - phase_stack: 3D numpy array (N_traps, res, res)
    - iters: Number of WGS iterations
    - desired_weights: 1D numpy array of desired relative trap intensities (optional)

    Returns:
    - slm_total_phase: final 2D phase pattern
    - uniformity: uniformity metric over iterations
    """
    N_holograms, res_x, res_y = phase_stack.shape
    pists = np.random.uniform(0, 2*np.pi, N_holograms)

    # Normalizzazione dei pesi target
    if desired_weights is not None:
        I_target = desired_weights / np.sum(desired_weights)
    else:
        I_target = np.ones(N_holograms) / N_holograms

    # Inizializzazione pesi
    weights = np.copy(I_target)

    uniformity = []
    intensities = []
    for i in range(iters):
        slm_total_field = np.sum(weights[:, None, None] * np.exp(1j * (phase_stack + pists[:, None, None])), axis=0)
        slm_total_phase = np.angle(slm_total_field)

        spot_fields = np.sum( np.exp(1j * (slm_total_phase[None, :, :] - phase_stack)), axis=(1, 2))
        pists = np.angle(spot_fields)

        I_measured = np.abs(spot_fields) ** 2
        intensities.append(I_measured)
        uniformity.append([1 - (np.max(I_measured) - np.min(I_measured)) / (np.max(I_measured) + np.min(I_measured))])

        # Weighted update using target intensities
        weights = weights * (np.sqrt(I_target) / np.sqrt(I_measured))
        weights = weights / np.sum(weights)  # Normalize total power

    return slm_total_phase, np.asarray(intensities).T