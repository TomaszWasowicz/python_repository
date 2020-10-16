def pyramid(letters: str):
    abc = letters
    len(abc)
    i = 0
    previous = ""
    space = " "
    while i < len(letters):
        actual = abc[0:i+1]
        print(space*(len(abc)-(i+1))+actual+previous)
        previous = actual[-1] + previous
        i += 1

pyramid(letters = ("abcdefg"))

