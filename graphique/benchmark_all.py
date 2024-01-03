import matplotlib.pyplot as plt

# Données pour l'addition
algorithmes = ["Concrete", "HElib", "OpenFHE", "SEAL", "TFHE"]
temps_addition = [0.03432059288, 5.97561e-05, 2e-8, 1.2e-5, 9.478239237]

# Données pour la multiplication
temps_multiplication = [0.0317943096, 0.00011775, 5.1e-8, 0.000457, 21.948282199]

# Créer les graphiques
plt.figure(figsize=(10, 5))
plt.title("Temps d'exécution de l'addition homomorphe")
plt.xlabel("Algorithme")
plt.ylabel("Temps (secondes)")
plt.yscale("log")
plt.bar(algorithmes, temps_addition)
plt.show()

plt.figure(figsize=(10, 5))
plt.title("Temps d'exécution de la multiplication homomorphe")
plt.xlabel("Algorithme")
plt.ylabel("Temps (secondes)")
plt.yscale("log")
plt.bar(algorithmes, temps_multiplication)
plt.show()
