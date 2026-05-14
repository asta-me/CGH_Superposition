# CGH_Superposition

Algoritmo generico di sovrapposizione per Computer Generated Holography (CGH).

## Cosa c'e nel progetto

Attualmente il repository contiene:
- `superpositions.py`: implementazione del metodo **Weighted Gerchberg-Saxton (WGS)**
	per la sintesi di ologrammi phase-only tramite sovrapposizione di maschere di fase.

L'approccio e generico e puo essere usato per target diversi, ad esempio:
- punti (array di trap ottiche),
- linee,
- pattern 2D arbitrari.

## Stato attuale

Per ora e implementato **solo il metodo WGS**.

## Sviluppi futuri

In futuro verranno aggiunti altri metodi, possibilmente **piu efficienti** e/o
**piu veloci**, per migliorare prestazioni, convergenza e flessibilita del workflow.
