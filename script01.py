#comando para instalar el modulo => pip install mysql-connector

import mysql.connector #importamos el modulo para conectar con mysql 

#Funcion para tratar los datos de str a float
def datos(x):

    res = 0
    var = []
    temp = 0.0
    for i in x:
        if i.isdigit() == 1:
            var.append(i)
    text = ''
    for element in var:
        text += element

    temp += float(text)/100
    return temp #DRetornamos el valor de la temperatura

def main():

    #Creamos una conexion con los datos del servidor y DDBB
    conn = mysql.connector.connect(host='localhost',user='root',passwd='',database='PI3')
    cursor = conn.cursor()

    #cursor.execute("show databases")

    #for b in cursor:
    #    print(b)

    print("\tPrograma para leer datos de arduino usando pyserial en tiempo real!\n\n")
    var = b'29.69\r\n'
    bytelist = [b'29.69\r\n',b'29.69\r\n',b'29.49\r\n',b'29.39\r\n',b'28.69\r\n',b'29.69\r\n',b'29.79\r\n'] #lista para simular los datos del arduino
    #string = "4.12232"
    #print(string+'a')
    #print(type(string))
    #newvar = float(string)
    #print(f"variable tipo: {type(newvar)} y valor nuevo es: {newvar}")
    #print(type(var))
    var2 = str(var)
    #print(type(var2))
    #print(var)
    #print(var2 + 'ggg')
    cont = 0 #contador para mantener el flujo de datos del arduino
    res = 0.0

    #ciclo donde hace el proceso principal
    while(cont<6):
        cont+=1
        #datos(var2)
        temp = datos(str(bytelist[cont])) #Guardamos los valores que retorna la funcion datos
        res += temp
        print(f"\tTu temperatura es: {temp} y tipo de dato: {type(temp)}") #imprimimos la temperatura y el tipo de dato

        query = "INSERT INTO `tabla01`(`sensor_data`) VALUES (%s)"%(temp) #query para insertar datos en la tabla
        cursor.execute(query) #ejecutamos
        conn.commit()
        print(f"Se han insertado {cursor.rowcount} dato en la BD")
    conn.close() #Cerramos la conexion
        

    print(res/6)



main()