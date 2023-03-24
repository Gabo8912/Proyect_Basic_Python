"""
PROYECTO INTEGRADOR
EQUIPO 5
Gabriel Alvarez - A01642991
Pavel Coutiño Peña - A01642589
Luis Ángel Aranda - A01642403
"""
def opciones(opc):#FUNCION QUE MUESTRA LAS OPCIONESDE REACTIVOS
    print("Opciones:\n1.-Matematicas\n2.-Español\n3.-Quimica\n0.-Salir")#OPCIONES
    opc=int(input("Ingresa la opcion deseada: "))#USUARIO INGRESA SU OPCION    
    return opc#SE REGRESA EL VALOR DE LA OPCION
    
def menu_principal(total_ejercicios,total_correctas,total_incorrectas):#FUNCION QUE INGRESA A LOS EJERCICIOS
    op=-1#VARIABLE DE OPCION CON UN VALOR CUALQUIERA 
    acum_correctas=0#ACUMULADOR INTERNO DE RESPUESTAS CORRECTAS
    acum_incorrectas=0#ACUMULADOR INTERNO RESPUESTAS INCONRRECTAS
    acum_ejercicios=0#ACUMULADOR INTERNO DE EJERCICIOS REALIZADOS
    while op!=0:#HACE EL CICLO MIENTRAS QUE EL USURIO NO INGRESE 0
        op=opciones(op)#SE LLAMA A LA FUNCION QUE MUESTRA LAS OPCIONES
        if op==1:#SI EL USARIO INGRESA LA OPCION 1 ENTRA 
            acum_ejercicios,acum_correctas,acum_incorrectas=mate(acum_ejercicios,acum_correctas,acum_incorrectas)#SE MANDAN LAS VARIABLES INTERNAS PARA QUE ACUMULEN
            total_ejercicios=total_ejercicios+acum_ejercicios#SE LES SUMA LOS VALORES A LAS VARIABLES GENERALES
            total_correctas=total_correctas+acum_correctas#SE LES SUMA LOS VALORES A LAS VARIABLES GENERALES
            total_incorrectas=total_incorrectas+acum_incorrectas#SE LES SUMA LOS VALORES A LAS VARIABLES GENERALES
        elif op==2:#SI EL USARIO INGRESA LA OPCION 2 ENTRA 
            acum_ejercicios,acum_correctas,acum_incorrectas=redaccion(acum_ejercicios,acum_correctas,acum_incorrectas)#SE MANDAN LAS VARIABLES INTERNAS PARA QUE ACUMULEN
            total_ejercicios=total_ejercicios+acum_ejercicios#SE LES SUMA LOS VALORES A LAS VARIABLES GENERALES
            total_correctas=total_correctas+acum_correctas#SE LES SUMA LOS VALORES A LAS VARIABLES GENERALES
            total_incorrectas=total_incorrectas+acum_incorrectas#SE LES SUMA LOS VALORES A LAS VARIABLES GENERALES
        elif op==3:#SI EL USARIO INGRESA LA OPCION 3 ENTRA 
            acum_ejercicios,acum_correctas,acum_incorrectas=quimica(acum_ejercicios,acum_correctas,acum_incorrectas)#SE MANDAN LAS VARIABLES INTERNAS PARA QUE ACUMULEN
            total_ejercicios=total_ejercicios+acum_ejercicios#SE LES SUMA LOS VALORES A LAS VARIABLES GENERALES
            total_correctas=total_correctas+acum_correctas#SE LES SUMA LOS VALORES A LAS VARIABLES GENERALES
            total_incorrectas=total_incorrectas+acum_incorrectas#SE LES SUMA LOS VALORES A LAS VARIABLES GENERALES
        elif op>3 or op<0:
            print("La opcion ingresada es invalida")#SE MUESTRA QUE EL USUARIO INGRESO UN VALOR ERRONEO
    return(total_ejercicios,total_correctas,total_incorrectas)#SE REGRESAN LOS VALORES DE LOS ACUMULADORES GLOBALES

def mate(acum_ejercicios,acum_correctas,acum_incorrectas):#FUNCION QUE MUESTRA EL TIPO DE EJERCIOS DE MATES
    print("Bienvenido!\nEntraste a los reactivos de mate, empecemos!")#SE LE DA LA BIENVENIDAD A MATE AL USUARIO
    op2=int(input("¿Deseas entrar a ejericios teoricos(1) o practicos(2), presiona 0 para salir?\nOpcion: "))#SE LE MUESTRA LA OPCION DE PRACTICOS O TEORICOS
    while op2!=0:#SE HACE EL CICLO MIENTRAS QUE EL USUARIO NO INGRESE 0
        if op2==1:#SI EL USUARIO INGRESA 1 SE HACEN LOS EJERCICIOS TEORICOS
            acum_ejercicios,acum_correctas,acum_incorrectas=teoricos_mate(acum_ejercicios,acum_correctas,acum_incorrectas)#SE MANDA LLAMAR LA FUNCION DE TERORICOS Y SE MANDAN LOS ACUMULADORES
            op2=int(input("¿Deseas entrar a ejericios teoricos(1) o practicos(2), presiona 0 para salir?"))#SE VUELVE A MOSTRAS LAS OPCIONES
        elif op2==2:#SI EL USUARIO INGRESA 2 SE HACEN LOS EJERCICIOS PRACTICOS
            acum_ejercicios,acum_correctas,acum_incorrectas=practicos_mate(acum_ejercicios,acum_correctas,acum_incorrectas)#SE MANDA LLAMAR LA FUNCION DE PRACTICOS Y SE MANDAN LOS ACUMULADORES
            op2=int(input("¿Deseas entrar a ejericios teoricos(1) o practicos(2), presiona 0 para salir?"))#SE VUELVE A MOSTRAS LAS OPCIONES
        else:
            op2=int(input("Opcion incorrecta!\n¿Deseas entrar a ejericios practicos(1) o teoricos(2)?, presiona 0 para salir"))#SE VUELVE A MOSTRAS LAS OPCIONES
        
    return(acum_ejercicios,acum_correctas,acum_incorrectas)#SE REGRESAN LOS VALORES MODIFICADOS DE LOS ACUMULADORES

def teoricos_mate(acum_ejercicios,acum_correctas,acum_incorrectas):#FUNCION DE LAS PREGUNTAS TEORICAS
    correctas=["a","b","c"]#LISTA CON LAS RESPUESTAS CORRECTAS
    acum_ejercicios=acum_ejercicios+3#SE LES SUMA 3 AL ACUMULADOR DE EJERCICIOS REALIZADOS
    i=0#VARIABLE QUE HACE LA VERIFICACION DE QUE PREGUNTA ESTAN Y RESPUESTA CORRECTA
    while i!=3:#SE HACE EL CICLO SIEMPRE QUE i NO LLEGUE A 3
        print(f"Preguta numero {i+1}")#SE MUESTRA EL NUMERO DE PREGUNTA QUE ES
        print("¿A que nos referimos con 'Es la razon de cambio instantaneo de una funcion matematica'? ")#SE MUESTRA LA PREGUNTA
        respuesta=input("Opciones:\na.-Derivada\nb.-Funcion\nc.-Ninguna opcion es correcta\nRespuesta: ")#SE MUESTRAN LAS OPCIONES DE RESPUESTA Y EL USUARIO INGRESA SU RESPUESTA
        if respuesta.lower()==correctas[i]:#SE HACE MINUSCULA LA RESPUESTA Y SE VERIFICA QUE LA RESPUESTA SEA CORRECTA
            print("Tu respuesta es correcta!")#SE LE INDICA AL USUARIO QUE SU RESPUESTA ES CORRECTA
            acum_correctas=acum_correctas+1#SE LE SUMA 1 AL ACUMULADOR DE RESPUESTAS CORRECTAS
            i=i+1#SE LE SUMA 1 A i
        else:
            print("Repuesta incorrecta!")#SE LE INDICA AL USUARIO QUE LA RESPUESTA ES INCORRECTA 
            acum_incorrectas=acum_incorrectas+1#SE LE SUMA 1 AL ACUMULADOR DE RESPUESTAS INCORRECTAS
            i=i+1
        print(f"Preguta numero {i+1}")#SE MUESTRA EL NUMERO DE PREGUNTA QUE ES
        print("¿Que tipo de recta es aquella que toca una curva en un unico punto? ")#SE MUESTRA LA PREGUNTA
        respuesta=input("Opciones:\na.-Recta secante\nb.-Recta Tangente\nc.-Rectas Paralelas\nRespuesta: ")#SE MUESTRAN LAS OPCIONES DE RESPUESTA Y EL USUARIO INGRESA SU RESPUESTA
        if respuesta.lower()==correctas[i]:#SE HACE MINUSCULA LA RESPUESTA Y SE VERIFICA QUE LA RESPUESTA SEA CORRECTA
            print("Tu respuesta es correcta!")#SE LE INDICA AL USUARIO QUE SU RESPUESTA ES CORRECTA
            acum_correctas=acum_correctas+1#SE LE SUMA 1 AL ACUMULADOR DE RESPUESTAS CORRECTAS
            i=i+1#SE LE SUMA 1 A i
        else:
            print("Repuesta incorrecta!")#SE LE INDICA AL USUARIO QUE LA RESPUESTA ES INCORRECTA 
            acum_incorrectas=acum_incorrectas+1#SE LE SUMA 1 AL ACUMULADOR DE RESPUESTAS INCORRECTAS
            i=i+1#SE LE SUMA 1 A i
        print(f"Preguta numero {i+1}")#SE MUESTRA EL NUMERO DE PREGUNTA QUE ES
        print("¿Que tipo de recta es aquella que corta una curva en dos puntos distintos?")#SE MUESTRA LA PREGUNTA
        respuesta=input("Opciones:\na.-Recta tangente\nb.-Recta Paralela\nc.-Recta Secante\nRespuesta: ")#SE MUESTRAN LAS OPCIONES DE RESPUESTA Y EL USUARIO INGRESA SU RESPUESTA
        if respuesta.lower()==correctas[i]:#SE HACE MINUSCULA LA RESPUESTA Y SE VERIFICA QUE LA RESPUESTA SEA CORRECTA
            print("Tu respuesta es correcta!")#SE LE INDICA AL USUARIO QUE SU RESPUESTA ES CORRECTA
            acum_correctas=acum_correctas+1#SE LE SUMA 1 AL ACUMULADOR DE RESPUESTAS CORRECTAS
            i=i+1#SE LE SUMA 1 A i
        else:
            print("Repuesta incorrecta!")#SE LE INDICA AL USUARIO QUE LA RESPUESTA ES INCORRECTA 
            acum_incorrectas=acum_incorrectas+1#SE LE SUMA 1 AL ACUMULADOR DE RESPUESTAS INCORRECTAS
            i=i+1#SE LE SUMA 1 A i
    return(acum_ejercicios,acum_correctas,acum_incorrectas)#REGRESA LOS ACUMULADORES YA MODIFICADOS
    
def practicos_mate(acum_ejercicios,acum_correctas,acum_incorrectas):#FUNCION QUE HACE LOS EJERCICIOS PRACTICOS Y RECIBE LOS ACUMULADORES
    correctas=["d","a","b"]#LISTA DE RESPUESTAS CORRECTAS
    acum_ejercicios=acum_ejercicios+3#SE LES SUMA 3 AL ACUMULADOR DE EJERCICIOS REALIZADOS
    i=0#SE LE ASIGNA EL VALOR DE 0 A i
    while i!=3:
        print(f"Preguta numero {i+1}")#SE MUESTRA EL NUMERO DE PREGUNTA QUE ES
        print("¿Cual es la derivada de la siguiente funcion y=x^4+3x^2-6")#SE MUESTRA LA PREGUNTA
        respuesta=input("Opciones:\na.-x\nb.-x^5+6\nc.-5x^5+3x\nd.4x^3+6x\nRespuesta: ")#SE MUESTRAN LAS OPCIONES DE RESPUESTA Y EL USUARIO INGRESA SU RESPUESTA
        if respuesta.lower()==correctas[i]:#SE HACE MINUSCULA LA RESPUESTA Y SE VERIFICA QUE LA RESPUESTA SEA CORRECTA
            print("Tu respuesta es correcta!")#SE LE INDICA AL USUARIO QUE SU RESPUESTA ES CORRECTA
            acum_correctas=acum_correctas+1#SE LE SUMA 1 AL ACUMULADOR DE RESPUESTAS CORRECTAS
            i=i+1#SE LE SUMA 1 A i
        else:
            print("Repuesta incorrecta!")#SE LE INDICA AL USUARIO QUE LA RESPUESTA ES INCORRECTA 
            acum_incorrectas=acum_incorrectas+1#SE LE SUMA 1 AL ACUMULADOR DE RESPUESTAS INCORRECTAS
            i=i+1#SE LE SUMA 1 A i
        print(f"Preguta numero {i+1}")#SE MUESTRA EL NUMERO DE PREGUNTA QUE ES
        print("Resuelve la siguiente ecuación de primer grado: 7(x+8)= -7")#SE MUESTRA LA PREGUNTA
        respuesta=input("Opciones:\na.-(-9)\nb.-4\nc.-(-6)\nd.-5\nRespuesta: ")#SE MUESTRAN LAS OPCIONES DE RESPUESTA Y EL USUARIO INGRESA SU RESPUESTA
        if respuesta.lower()==correctas[i]:#SE HACE MINUSCULA LA RESPUESTA Y SE VERIFICA QUE LA RESPUESTA SEA CORRECTA
            print("Tu respuesta es correcta!")#SE LE INDICA AL USUARIO QUE SU RESPUESTA ES CORRECTA
            acum_correctas=acum_correctas+1#SE LE SUMA 1 AL ACUMULADOR DE RESPUESTAS CORRECTAS
            i=i+1#SE LE SUMA 1 A i
        else:
            print("Repuesta incorrecta!")#SE LE INDICA AL USUARIO QUE LA RESPUESTA ES INCORRECTA 
            acum_incorrectas=acum_incorrectas+1#SE LE SUMA 1 AL ACUMULADOR DE RESPUESTAS INCORRECTAS
            i=i+1#SE LE SUMA 1 A i
        print(f"Preguta numero {i+1}") #SE MUESTRA EL NUMERO DE PREGUNTA QUE ES
        print("Resuelve la ecucacion de segundo grado:\nx^2-5x+6")#SE MUESTRA LA PREGUNTA
        respuesta=input("Opciones:\na.-x1=9,x2=-8\nb.-x1=3,x2=2\nc.-x1=0,x2=0\nd.-x1=12,x2=5\nRespuesta: ")#SE MUESTRAN LAS OPCIONES DE RESPUESTA Y EL USUARIO INGRESA SU RESPUESTA
        if respuesta.lower()==correctas[i]:#SE HACE MINUSCULA LA RESPUESTA Y SE VERIFICA QUE LA RESPUESTA SEA CORRECTA
            print("Tu respuesta es correcta!")#SE LE INDICA AL USUARIO QUE SU RESPUESTA ES CORRECTA
            acum_correctas=acum_correctas+1#SE LE SUMA 1 AL ACUMULADOR DE RESPUESTAS CORRECTAS
            i=i+1#SE LE SUMA 1 A i
        else:
            print("Repuesta incorrecta!")#SE LE INDICA AL USUARIO QUE LA RESPUESTA ES INCORRECTA 
            acum_incorrectas=acum_incorrectas+1#SE LE SUMA 1 AL ACUMULADOR DE RESPUESTAS INCORRECTAS
            i=i+1#SE LE SUMA 1 A i
    return(acum_ejercicios,acum_correctas,acum_incorrectas)#REGRESA LOS ACUMULADORES YA MODIFICADOS

def redaccion(acum_ejercicios,acum_correctas,acum_incorrectas): #definimos la parte de redaccion
    print('Se denomina redacción al proceso mediante el cual se estructura un discurso escrito.') #se da una breve introduccion al tema 
    print('La redacción es un arte, pero también una técnica. Es la medida que utiliza determinados procederes que garantizan que el texto tenga coherencia.')
    espacio= ' . .  ' #separaciones con puntos usando for
    for punto in range(len(espacio)): 
        print(espacio[punto])
    print('A continuacion contestaras un quiz sobre redaccion: ') #dar continuacion al examen 
    for punto in range(len(espacio)): #ponemos la separacion de los puntos
        print(espacio[punto])
#valores
    correctas=['a','b','a'] #introducimos las respuestas en una lista dentro de una variable
    i=0
#lanzar resultados y preguntas
    while i!=3: #usar while para dar respuesta a las preguntas
        redaccion=(input(f'Pregunta {i+1}\n¿Que es la redaccion? \n a).- proceso mediante el cual se estructura un discurso escrito. \n b).- un texto que se crea y tiene coherencia. \n c).- una forma de hablar de arte en un texto. \n R= '))
        if redaccion.lower() == correctas[i]: #ponemos lower para hacer la respuesta en minuscula 
            print('Correcto')
            acum_correctas+=1 #acumula las respuestas
        else:
            print('Incorrecto')
            acum_incorrectas+=1 #acumala las respuestas incorrectas 
        i=i+1;
        semantica=(input(f'Pregunta {i+1}\n¿Que es la semantica? \n a).- Es la ciencia linguistica que estudia los campos de la linguistica. \n b).- Es la ciencia linguistica que estudia el significado de palabras y expresiones. \n c).- Es una tecnica para crear textos. \n R= '))
        if semantica.lower() == correctas[i]: #ponemos lower para hacer la respuesta en minuscula
            print('Correcto')
            acum_correctas+=1 #acumula las respuestas correctas
        else:
            print('Incorrecto')
            acum_incorrectas+=1 #acumula las respuestas incorrectas
        i=i+1
        inferencia=(input(f'Pregunta {i+1}\n¿Que es la inferencia? \n a).- concluir o decidir a partir de algo conocido o asumido. \n b).- Es una tecnica de la linguistica para tener coherencia. \n c).- Es la forma de ver un texto y entenderle. \n R= '))
        if inferencia.lower() == correctas[i]: #ponemos lower para hacer la respuesta en minuscula
            print('Correcto')
            acum_correctas+=1 #acumula las respuestas correctas
        else:
            print('Incorrecto')
            acum_incorrectas+=1 #acumula las respuestas incorrectas
        i=i+1
        op3=int(input("¿Quieres volver a intentarlo?(1.-Si,2.-No): ")) #dan la opcion de volver a intentar el examen
        if op3==1:
            i=0
        acum_ejercicios=acum_ejercicios+3 #acumula los ejercicios 
    print("¡Bien hecho!")
    return(acum_ejercicios,acum_correctas,acum_incorrectas)#REGRESA LOS ACUMULADORES YA MODIFICADOS

def quimica(acum_ejercicios,acum_correctas,acum_incorrectas):
    
    print("¡Bienvenido a la sección de ciencias!") 
    correctas=["a","b","c"] #lista con las respuestas correctas
    acum_ejercicios=acum_ejercicios+3 #se le suma 3 al acumulador de ejercicios realizados
    i=0
    while i!=3: #se hace el ciclo mientras i no sea otro más que 3
        acum_ejercicios=acum_ejercicios+3
        print(f"Preguta numero {i+1}") #muestra el número de pregunta, en este caso es el 1
        print("¿Qué son los números cuánticos?: ") #se despliega la pregunta numero 1 como tal
        respuesta=input("Opciones:\na.-Son valores numéricos discretos que indican las características de los electrones en los átomos\nb.-Compuestos orgánicos derivados de petróleo o inorgánicos oxigenados en los cuales uno o más grupos hidroxilos son sustituidos por grupos orgánicos alquilo\nc.-Ninguna opcion es correcta\nRespuesta: ")
        if respuesta.lower()==correctas[i]: #se hace minúscula la respuesta y se verifica que sea correcta
            print("Tu respuesta es correcta!")
            acum_correctas=acum_correctas+1
            i=i+1 #se le suma 1 al acumulador de respuestas correctas
        else:
            print("Repuesta incorrecta!") #se le indica al usuario que la respuesta es incorrecta
            acum_incorrectas=acum_incorrectas+1 
            i=i+1 #se le suma 1 al acumulador de respuestas incorrectas
        print(f"Preguta numero {i+1}") #se muestra el numero de pregunta que es, en este caso es el número 2
        print("¿Qué es rápidez promedio?: ") #se imprime la pregunta
        respuesta=input("Opciones:\na.-Derivada de la función de velocidad\nb.-Relación entre la distancia total recorrida y el tiempo total empleado durante 'todo' el viaje\nc.-Ninguna de las anteriores\nRespuesta: ")
        if respuesta.lower()==correctas[i]: #se hace minúscula la respuesta y se verifica que sea correcta
            print("Tu respuesta es correcta!") #la respuesta es correcta
            acum_correctas=acum_correctas+1
            i=i+1 # se le suma 1 al acumulador de respuestas correctas
        else:
            print("Repuesta incorrecta!") #se le indica al usuario que la respuesta es incorrecta
            acum_incorrectas=acum_incorrectas+1
            i=i+1 # se le suma 1 al acumulador de respuestas incorrectas
        print(f"Preguta numero {i+1}") # se indica el número de pregunta, en este caso el número 3
        print("¿Qué es densidad?: ") # se imprime la pregunta
        respuesta=input("Opciones:\na.-Magnitud física y propiedad general de la materia​ que expresa la inercia o resistencia al cambio de movimiento de un cuerpo\nb.-Medida de la fuerza gravitatoria que actúa sobre un objeto\nc.-Volumen de una sustancia o un objeto sólido\nRespuesta: ")
        if respuesta.lower()==correctas[i]: # se hace minúscula la respuesta y se verifica que sea correcta
            print("Tu respuesta es correcta!") #imprime que la respuesta es correcta
            acum_correctas=acum_correctas+1
            i=i+1 #se le suma 1 al acumulador de respuestas correctas
        else:
            print("Repuesta incorrecta!") #imprime que la respuesta es incorrecta
            acum_incorrectas=acum_incorrectas+1
            i=i+1 #se le suma 1 al acumulador de respuestas incorrectas
        op3=int(input("¿Quieres volver a intentarlo?(1.-Si,2.-No)"))
        if op3==1:
            i=0
    return(acum_ejercicios,acum_correctas,acum_incorrectas)#REGRESA LOS ACUMULADORES YA MODIFICADOS


total_ejercicios=0#ACUMULADOR DE EJERCICIOS GLOBAL
total_correctas=0#ACUMULADOR DE RESPUESTAS CORRECTAS GLOBAL
total_incorrectas=0#ACUMULADOR DE RESPUESTAS INCORRECTAS GLOBAL
print("Bienvenido a este programa que te ayudara a estudiar matematicas, español y quimica")
total_ejercicios,total_correctas,total_incorrectas=menu_principal(total_ejercicios,total_correctas,total_incorrectas)#SE LE LLAMA A FUNCION DEL MENU PRINCIPAL MANDANDO LOS ACUMULADORES GLOBALES
print(f"El total de ejercicios relizados es: {total_ejercicios}\nEl total de respuestas correctas es: {total_correctas}")#SE MUESTRA LOS EJERCIOS CORRECTO Y RESPUESTAS CORRECTAS
print(f"El total de respuestas incorrectas es: {total_incorrectas}")#SE MUESTRAN LAS RESPUESTAS TOTALES INCORRECTAS
print("Gracias por practicar con nosotros!, mucha suerte!\nSaliendo del sistema...")#SE DESPIDE DEL PROGRAMA