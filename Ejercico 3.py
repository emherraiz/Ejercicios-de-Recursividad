def bandera(colores, i = 0, rojo = list(), verde = list(), azul = list(), no_pertenece = 0):
    if i != len(colores):
        if colores[i] == 'R':
            rojo.append(colores[i])
        elif colores[i] == 'G':
            verde.append(colores[i])
        elif colores[i] == 'B':
            azul.append(colores[i])
        else:
            no_pertenece += 1

        i += 1
        bandera(colores, i, rojo, verde, azul, no_pertenece)
    return rojo, verde, azul, no_pertenece

# Esta lista la puedes modificar para obtener diferentes resultados
colores = ['R','B','B','R', 'G']

rojo, verde, azul, no_pertenece = bandera(colores)
flag = rojo + verde + azul
print(flag)
print(f'Hay {no_pertenece} fichas con un color que no pertenece a la bandera')


