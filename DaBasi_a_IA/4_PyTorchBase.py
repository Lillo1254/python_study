# PyTorch p lo standard per la ricerca e sviluppo di modelli complessi poiche possiede due librerie per reindirizzamente uso memorie GPU e CPU e differenziazione automatica per il calcolo delle derivate degli errori la sintassi di PyTorch è stata progettata per essere identica a quella di NumPy
import torch
import numpy as np

# Creare un tensore da zero in PyTorch metodo torch.tensor()
tensore_pt = torch.tensor([1.0, 2.0, 3.0])
print(f"Tensore PyTorch: {tensore_pt}")
print(f"Tipo oggetto: {type(tensore_pt)}")

# Convertire un array NumPy esistente in un tensore PyTorch
array_np = np.array([10, 20, 30])
# possiamo creare un tensore utilizzando la funzione torch.from_numpy che converte un array NumPy esistente in un tensore PyTorch mantenendo la stessa memoria di riferimento quindi modificando l'array NumPy modifichiamo anche il tensore PyTorch
tensore_da_np = torch.from_numpy(array_np)
print(f"Convertito in PyTorch: {tensore_da_np}")

# Per leggere la forma di un tensore possiamo usare il metodo .shape ma in pytorch lo standard nativo per la stessa operazione è il metodo .size()
print(f"Forma del tensore .shape: {tensore_pt.shape}")
print(f"Forma del tensore .size: {tensore_pt.size()}")