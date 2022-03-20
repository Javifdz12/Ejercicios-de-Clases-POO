class palindromo:

    def esPalindromo(palabra):
        comprobar = True
        izquierda= 0
        derecha= len(palabra)-1

        while izquierda != derecha:
            if palabra[izquierda] == palabra[derecha]:
                izquierda = izquierda + 1
                derecha = derecha - 1
            else:
                comprobar = False
                break

        if comprobar == True:
            return True
        else:
            return False

print(palindromo.esPalindromo("radar"))
print("pene")