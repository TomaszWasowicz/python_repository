def missing_codes(code1, code2):
    parse = lambda x: int(x.replace('-', ''))
    code1, code2 = parse(code1), parse(code2)
    return ["%02d-%03d" % divmod(x, 1000) for x in range(code1 + 1, code2)]


print(missing_codes("79-900", "80-155"))
