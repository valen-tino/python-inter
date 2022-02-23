# ini hanya komentar
def main():
    celcius = eval(input("Masukkan nilai celcius : "))
    fahrenheit = (9/5) * celcius + 32
    print ("Fahrenheit : " + str(fahrenheit))

    fahrenheit = eval(input("Masukkan nilai fahrenheit : "))
    celcius = (fahrenheit - 32) * (5/9)
    print ("Celcius : " + str(celcius))
main()