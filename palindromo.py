word="radar"
def palindromo(word):
    inverse=word[::-1]
    if inverse == word:
        print(f"la palabra {word} es un palindromo")
    else: 
         print(f"la palabra {word} no es un palindromo")

palindromo("hola")

