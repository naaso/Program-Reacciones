from Entrada import f_Entrada
def Start(start):
    if start=="yes":
        L_viga=int(input("Ingrese la longitud de la viga: "))
        n_cargas=int(input("Numero de cargas: "))
        D_cargas=[]
        By=[]
        Ay=[]
        for i in range(n_cargas):
            Carga=tuple(f_Entrada(input("Tipo de carga: ")))
            D_cargas.append(Carga)

        for i in range(n_cargas):

            if D_cargas[i][0]=="puntual":
                puntual=D_cargas[i]
                t,k,a=puntual
                by=(k*a)/L_viga
                By.append(by)
                ay=k-by
                Ay.append(ay)
                
            elif D_cargas[i][0]=="distribuida uniforme":
                d_t=D_cargas[i]
                t,a,b,h1=d_t
                by=((b*h1)*((b/2)+a))/L_viga
                By.append(by)
                ay=(b*h1)-by
                Ay.append(ay)
            #casos
            elif D_cargas[i][0]=="distribuida trapezoidal":
                d_t=D_cargas[i]
                t,a,h1,b,h2=d_t
                if h2>h1:
                    x_c=((h1*b*b)/2+(((2/3)*b*b*(h2-h1))/2))/(h1*b+((h2-h1)*b)/2)
                else:
                    x_c=((h2*b*b)/2+(((1/3)*b*b*(h1-h2))/2))/(h2*b+((h1-h2)*b)/2)
                    
                by=(b/L_viga)*((h1+h2)/2)*(x_c+a)
                ay=b*((h1+h2)/2)-by
                By.append(by)
                Ay.append(ay)
                
            elif D_cargas[i][0]=="distribuida triangular":  
                d_t=D_cargas[i]
                t,h1,a,b=d_t
                if b>a:
                    by=((((b-a)*h1)/2)*((2/3)*(b-a)+a))/L_viga
                    ay=(((b-a)*h1)/2)-by
                else:
                    by=((((a-b)*h1)/2)*((1/3)*(a-b)+b))/L_viga
                    ay=(((a-b)*h1)/2)-by
                By.append(by)
                Ay.append(ay)
                
            else:
                print("ingresa una carga válida")
        By=sum(By)
        Ay=sum(Ay)
        print(f"Ay={Ay}, By={By}")

start=Start(start=input(f'''Este es un programa para el cálculo de reacciones en vigas simplemente apoyadas para cargas puntuales y distribuidas de tipo:
uniforme, triangular y trapezoidal, para acceder a las anteriores escribe: distribuida y el tipo (antes dichos). Para empezar escribe "yes": ''' ))
