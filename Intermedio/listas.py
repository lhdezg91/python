
my_original_list = [1, 2, 3, 4, 5]

new_list = [i for i in my_original_list]
#esto es equivalente a: new_list = my_original_list

new_list = [i*2 for i in my_original_list]
#esto es equivalente a: cada elemento antes de guardarlo en la nueva lista se multiplica por 2

new_list = [i for i in my_original_list if i % 2 == 0]
#esto es equivalente a: se guardan solo los elementos pares

new_list = [i for i in my_original_list if i % 2 != 0]
#esto es equivalente a: se guardan solo los elementos impares

new_list = [i**2 for i in my_original_list]
#esto es equivalente a: se guardan los elementos al cuadrado

def cuadrado(x):
    return x**2

new_list = [cuadrado(i) for i in my_original_list]
#esto es equivalente a: se guardan los elementos al cuadrado

