#Program zip-code
#Napisany przez Tomasza Wąsowicza

while True:
    try:
        zip_code = str(input("Type a zipcode with a following combination: digit digit - digit digit digit: "))
        if not len(zip_code) == 6:
            raise ValueError
        if zip_code[2] != "-":
            raise ValueError
        if not (zip_code[0:2]):
            raise ValueError
        print("Zipcode is correct")
        break

    except ValueError:
        print("Zip Code has 5 letters")

