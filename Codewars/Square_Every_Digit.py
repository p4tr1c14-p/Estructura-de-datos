def square_digits(num):
    result = ""  # Variable para guardar el resultado
    for digit in str(num):  # Iteramos sobre cada carácter del número convertido a cadena
        result += str(int(digit) ** 2)  # Cuadramos el dígito y lo concatenamos a 'result'
    return result  # Retornamos el resultado final como una cadena
num= int(input("Ingrese num: "))