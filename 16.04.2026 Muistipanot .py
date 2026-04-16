def hello_world(code):
    if code == 'fi':
        return("Hei maailma!")
    elif code == 'en':
        return("Hello world!")
    elif code == 'sv':
        return("Hej världen!")
    elif code == 'es':
        return("¡Hola mundo!")
    else:
        return("Unknown language code.")

a = input("Enter language code (fi, en, sv, es): ")
print(hello_world(a))
