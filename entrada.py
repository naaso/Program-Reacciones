def f_Entrada(t_carga):
#entrada de datos
    d_carga=[]
    if t_carga=="puntual":
        d_carga.append(t_carga)
        k=float(input("Valor de la carga: "))
        d_carga.append(k)
        a=float(input("Distancia hacia la carga desde el primer apoyo: "))
        d_carga.append(a)
    if t_carga=="distribuida uniforme":
        d_carga.append(t_carga)
        a=float(input("Distancia hacia la carga desde el primer apoyo: "))
        d_carga.append(a)
        b=float(input("Longitud de la carga: "))
        d_carga.append(b)
        h1=float(input("Valor de la carga: "))
        d_carga.append(h1)
    if t_carga=="distribuida triangular":
        d_carga.append(t_carga)
        h1=float(input("Valor de la carga: "))
        d_carga.append(h1)
        a=float(input("Distancia hacia la carga cero desde el apoyo izquierdo: "))
        d_carga.append(a)
        b=float(input("Distancia hacia la carga desde el apoyo izquierdo: "))
        d_carga.append(b)
    if t_carga=="distribuida trapezoidal":
        d_carga.append(t_carga)
        a=float(input("Distancia hacia la carga desde el primer apoyo: "))
        d_carga.append(a)
        h1=float(input("Valor de la carga 1: "))
        d_carga.append(h1)
        b=float(input("Longitud de la carga: "))
        d_carga.append(b)
        h2=float(input("Valor de la carga 2: "))
        d_carga.append(h2)
              

    return d_carga