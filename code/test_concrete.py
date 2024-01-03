from concrete import fhe
import time

#fonction d'addition et multiplication
def add(x, y):
    return x + y

def mul(x, y):
    return x * y

#temps python addition et multiplication sans concrete
#addition normal
start = time.time()
print("4+4 = ", add(4,4))
end = time.time()
print("Temps que prend l'addition en python sans concrete : " , end - start)

#multiplication normal
start = time.time()
print("4*4 = ", mul(4,4))
end = time.time()
print("Temps que prend la multiplication en python sans concrete : ", end - start)

#temps python addition et multiplication avec concrete:
#addition concrete

start = time.time()

compiler = fhe.Compiler(add, {"x": "encrypted", "y": "clear"})

inputset = [(2, 3), (0, 0), (1, 6), (7, 7), (7, 1)]
circuit = compiler.compile(inputset)

x = 4
y = 4

clear_evaluation = add(x, y)
homomorphic_evaluation = circuit.encrypt_run_decrypt(x, y)
end = time.time()
print(x, "+", y, "=", clear_evaluation, "=", homomorphic_evaluation)
print("l'algorithme addition avec Concrete à pris : ",end - start," sec")

#multiplication concrete
start = time.time()

compiler = fhe.Compiler(mul, {"x": "encrypted", "y": "clear"})

inputset = [(2, 3), (0, 0), (1, 6), (7, 7), (7, 1)]
circuit = compiler.compile(inputset)

x = 4
y = 4

clear_evaluation = mul(x, y)
homomorphic_evaluation = circuit.encrypt_run_decrypt(x, y)
end = time.time()
print(x, "+", y, "=", clear_evaluation, "=", homomorphic_evaluation)

print("l'algorithme multiplication avec Concrete à pris : ",end - start," sec")

