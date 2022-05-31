#     30-11-2021   Ejercicios Tema 3
"""1. Crear las siguientes expresiones regulares:
    - Correo electrónico.
    - Hash en MD5 (32 caracteres)
    - Matrícula de avión: uno o dos letras mayúsculas, guión medio y 3 letras mayúsculas.
    - Dirección IP v6.
Hay que ponerlas en una variable cada una de ellas.

2. Crear una clase llamada ValidarER que permitirá validar una expresión regular frente a un
ejemplo usando la librería re.
    - Constructor: recibirá un texto con la expresión regular, además deberá definir una lista
    para guardar cada operación que se realiza en el método Validar, es decir guardar cada
    ejemplo remitido y contra que expresión se está validando, así como su resultado.  
    - ModificarER: que cambiará la expresión regular actual por una que recibirá.
    - Validar: recibirá un texto de ejemplo y devolverá true si el texto de ejemplo valida
    contra la expresión regular. En caso contrario devolverá un false.
    - Deberá contener un método para imprimir la expresión regular.
    - Deberá validar todas las expresiones del apartado 1 a través de un objeto de esta clase.

3. Crear una clase para generar un self.correo electrónico del dominio xxxxx@ecorp.com.
    - Constructor: deberá recibir los datos del usuario (nombre, apellidos, dni).
    - GenerarCorreo: deberá generar un self.correo electrónico con el siguiente patrón:
        - dos primera iniciales del nombre.
        - primer apellido.
        - primera inicial del segundo apellido.
        - dos últimos números del dni.
        - @ecorp.com
    - ValidarCorreo: deberá validar la cuenta generada contra el patrón de self.correo electrónico
    a través del objeto de la clase ValidarER generado en el 2º apartado y que recibirá
    por parámetro en el método.  

4. Añadir un argumento de entrada opcional que indicará si se desea hacer un volcado del
histórico de expresiones validadas en un fichero. Si viene a "S" o "s" deberá recorrer el
histórico del objeto generado en el apartado 2 y escribir en cada línea la expresión regular
utilizada, el ejemplo para validar y el resultado, todo ello separado por ;
Ejemplo:  [0-1];1;True"""
import exrex,hashlib,re,os,argparse

print("\t\tEjercicio 1")
correolandia = ".{1,10}@((protonmail\.com)|(ecorp\.(us|com)))"
ej_correo = exrex.getone(correolandia)
print ("\n\n\tun ejemplo de self.correo es " + ej_correo)
MD5 = hashlib.md5()
MD5.update(b"samsepi0l@ecorp.us")
print("\nHash de Eliot MD5 generado como "+MD5.hexdigest())
B777 = "[A-Z]{1,2}-[A-Z]{3}"
pista = ("[1-5]{1,2}")
# esto es la matrícula de avión, y una pista cualquiera
print("\nBoeing 777 con matrícula\t" +exrex.getone(B777)+"\t tiene permiso para despegar por la pista  "+exrex.getone(pista))
#IPv6    wa40::3cs0:9rh0:6d5:2576%4   he visto otros ejemplos con distinto numero de caracteres en cada campo entre los : pero tomaré este como ejemplo
#IPv6 = "(([a-z])|([0-9])){4}::(([a-z])|([0-9])){4}:(([a-z])|([0-9])){4}:(([a-z])|([0-9])){3}:(([a-z])|([0-9])){4}%[0-9]"
#print("ipv6 es "+ (exrex.getone(IPv6)))     me acabo de dar cuenta que aunque esto me hubiera servido perfectamente, si nos ponemos quisquillosos una IPv6 en condicinones es así https://docs.oracle.com/cd/E19957-01/820-2981/6nei0r0ue/index.html
# a ver si genero en hexadecimal todos hasta 48 bits   // let's try generating all hex adresses till 48 bits

#esto era de prueba, así que copio la ex regular del sitio https://www.dokry.com/3502      //  just testing, copied regular ex from that URL
#print("\n\t\t48 en hexa es "+hex(1))
#print("\n"+ hex(2))
IPv6 = "(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"
print("\n\t\tUna IPv6 válida podría ser\t"+ exrex.getone(IPv6))  #bueno vale, pensandolo mejor, este ejemplo no es realmente adecuado pues hay campos que van "juntos" para formar un número, y aquí se podrían exceder pero bueno,a mi criterio por lo menos me sirve

# por lo que he leído tanto en esa página de donde saqué esta expresión regular, como de la página https://gist.github.com/syzdek/6086792 resulta que generar TODAS las posibles IPv6 es muy muy difícil, me da que en esa pregunta os habéis calentado un poco :-|    
#Ahora          EJERCICIO 2

textoER = "info@((kaspersky\.com)|(ecorp\.(us|com)))"
nuevaER = "info@((avast\.com)|(ecorp\.(eu|es)))"
ejemplar = "info@kaspersky.com"
print("\n\t\tEjercicio 2")
v_lista = []  # me temo que si no lo defino también aquí aparte de en ValidarER, no puedo usar v_lista en argumentos de entrada
class ValidarER:
    def __init__(self,textoER):
        self.textoER = textoER
        v_lista = []
    def ModificarER(self,nuevaER):
        self.textoER = nuevaER      #cambio la variable/atributo interno self.textoER por el valor que tenga nuevaER
        print("\nahora self.textoER osea la lueva ex regular es  "+self.textoER)
    def Validar(self,ejemplar):
        if (re.fullmatch(self.textoER, ejemplar, flags=0)):
            print("RE.fullmatch funciona!!!\tParece que sirve para expresiones regulares")
        #al principio lo hice con la línea de abajo, con "if" y un "in" para comprobar, pero he visto que re.fullmatch también va   https://docs.python.org/3.9/library/re.html?highlight=re%20fullmatch#re.fullmatch   // also coded comparison using "if" and "in" but seems that code from this URL also works
            """if ejemplar in exrex.generate(textoER):"""
            print("\n\tPatata caliente, hay una coincidencia de 'ejemplar' en 'textoER', es\t"+textoER)
            v_lista.append([ejemplar,str(self.textoER),"True"])                                     # en la lista, guardaré tuplas, cada una contine 3 cosas: el ejemplo remitido, la expresión, y el resultado de la comparación
        else:
            print("\n\tPatata quemada. No se ha encontrado 'ejemplar':\t"+ejemplar+"\ten las posibilidades de la ex regular 'textoER'")
            v_lista.append([ejemplar,str(self.textoER),"False"])
        print("\n\n\t\tla lista v_lista es:\t"+str(v_lista))
    def ImprimeER(self,textoER):
        print("\n\n\tAhora la ex regular es:\t"+self.textoER)
probandoValidarER = ValidarER(textoER)
probandoValidarER.Validar(ejemplar)
probandoValidarER.ModificarER(nuevaER)
probandoValidarER.Validar(ejemplar)
probandoValidarER.ImprimeER(textoER)
os.system("pause")
                        #EJERCICIO 3 
dni = "51010134E"
nombre = "Jaime"
ape1= "de_Gaulle"
ape2= "Ortega"
correo = ""
print("\n\t\tEjercicio 3")
class Correo:
    def __init__(self,nombre, ape1, ape2,dni,correo): 
        self.nombre = nombre
        self.ape1 = ape1
        self.ape2 = ape2
        self.dni = dni
        self.correo = correo
    def GenerarCorreo(self):
        self.correo = self.nombre[:2]
        self.correo = (self.correo + self.ape1)
        self.correo = (self.correo + self.ape2[0])
        self.correo = (self.correo + self.dni[6:8])     # de aquí entiendo que el dni siempre tendrá 8 posiciones, no hay otra   // i guess national ID has 8 characters, otherwise no way
        self.correo = (self.correo + "@ecorp.com")
        print("\nel correo es\t" + self.correo)
    def ValidarCorreo(self,probandoValidarER):
        ex_reg_correo =  (self.nombre[:2] + self.ape1+self.ape2[0]+self.dni[6:8]+"@ecorp\.com")#".{1,10}@((protonmail\.com)|(ecorp\.(us|com)))"
        centralita = exrex.generate(ex_reg_correo)
        for self.sello in centralita:
            if self.correo == str(self.sello):
                print("\nPatata, hay una coincidencia, en el correo a validar y la expresión (la única coincidencia posible, centralita tiene 1 único valor)  ✌(-‿-)✌")   
            else:
                print("\nHoy no hay patatas\t"+ self.sello)
            #he hecho la comparación aquí, ahora voy con el objeto de la clase ValidarER    //  just made comparison here, so, now let's get object from class ValidarER
            probandoValidarER.Validar(ejemplar)                                            # me da que algo mal hice en esta línea  // maybe i did something wrong in this file
objetoCorreo=Correo(nombre,ape1,ape2,dni,correo)
objetoCorreo.GenerarCorreo()
objetoCorreo.ValidarCorreo(probandoValidarER)

                        #EJERCICIO 4
"""
parser=argparse.ArgumentParser()

parser.add_argument("-f","--dump",type=str,required=True,help="dump or not reg expressions and examples history",dest="Dump")
args=parser.parse_args()
#primero intentar crear el fichero
if args.Dump == "S" or args.Dump == 's':
        try:

            file = open('Ejs_T3_regular_expresions.txt', "x")

            file.close()

        except:

            print("\n\nEL FICHERO YA EXISTE")

        finally:

            print("\n\nFICHERO EXISTENTE")

        try:
            file = open('Ejs_T3_regular_expresions.txt', "r+")
            print("v_lista es\t"+str(v_lista))
            for a in v_lista:
                for b in a:
                    if b != "False" and b != "True":
                        file.write(b+";")
                    else:
                        file.write(b+"\n")   # está a propósito, para no imprimir el último ; al final de cada línea
            file.close()
        except:
            print("\n\n\tAlgo ha fallado en escribir en el fichero....")
#  re.fullmatch(pattern, string, flags=0)
#If the whole string matches the regular expression pattern, return a corresponding match object. Return None if the string does not match the pattern; note that this is different from a zero-length match.
                """  #sencillamente, esta parte metida en string sin asignar a ninguna variable, no se puede usar sin otro archivo necesario. Adjuntado en Github igualmente
                     #just commented code, so it doesn't crash due to missing file. This file is uploaded to Github anyway if u want to make changes
#               https://docs.python.org/3.9/library/re.html?highlight=re%20fullmatch#re.fullmatch