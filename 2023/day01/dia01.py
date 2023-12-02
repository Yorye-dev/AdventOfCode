# Objetivo, tenemos una lista de caracteres, compuestos por numeros y letras, y queremos de cada linea del listado aportado por un txt,
# queremeos alamacenar el primer valor numerico y concateneralo con el segundo. En caso de solo haber un unico valor, se concatenará así mismo
# Todos los resultados se almacenaran en una array y luego se sumarán.

def getNumberOfString(cadena):
    numString =""
    list_of_num = []
    isTheLastOne=False
    isTheFirstOne=False
    theFirstNumber=""
    longString = len(cadena)
    for i, char in enumerate(cadena):
        if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if isTheFirstOne == False and isTheLastOne == False: 
                isTheFirstOne = True
                numString = numString + char
                theFirstNumber = char
            elif isTheFirstOne == True and isTheLastOne == False:
                isTheLastOne = True
                numString = theFirstNumber + char
            elif isTheFirstOne == True and isTheLastOne == True:
                numString = theFirstNumber + char
                
    if len(numString) == 0:
        numString = "0"
        print(" En la cadena " +cadena+ "no hay numeros")
        return numString
    elif len(numString) == 1:
        numString =numString + numString
        print(" En la cadena " +cadena+ " solo hay un numero por lo cual el resultado es: " + numString)
        return numString      
    else:
        print(" En la cadena " +cadena+ " se encunetran los siguientes numeros: " + numString)
        return numString

def sumListOfStringOfNumber(listOfNUmberAsStrings):
    totalNun = 0
    for i, sublista, in enumerate(listOfNUmberAsStrings):
        totalNun = totalNun + int(listOfNUmberAsStrings[i])
    return totalNun


list_of_num = []
result = 0
entrada = 'entrada.txt' # Fichero de emtrada
try:

    with open(entrada, 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
        # Elimina los espacios en blanco y caracteres de nueva línea
            stringOfTheTxt = linea.strip()
            # Llama al método proporcionado con el elemento actual
            list_of_num = list_of_num + [getNumberOfString(stringOfTheTxt)]
    result = sumListOfStringOfNumber(list_of_num)
    print("------------------------------------")
    print(result)

except FileNotFoundError:
    print(f"El archivo '{entrada}' no fue encontrado.")


