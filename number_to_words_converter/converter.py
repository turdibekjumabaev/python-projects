"""
Number to words converter
Developer: Turdıbek Jumabaev
"""

def convert_number_to_words(n):
    """Sandı textge awdarma islep beredi"""

    # birlikler
    ones = ["", "bir", "eki", "úsh", "tórt", "bes", "altı", "jeti", "segiz", "toģız", "on"]

    # onlıqlar
    tens = ["", "on", "jigirma", "otız", "qırıq", "eliw", "alpıs", "jetpiz", "seksen", "toqsan"]

    if n < 10:
        return ones[n]
    if n < 100:
        return tens[n // 10] + ('' if n % 10 == 0 else ' ' + ones[n % 10])
    if n < 1000:
        return ones[n // 100] + ' júz' + ('' if n % 100 == 0 else ' ' + convert_number_to_words(n % 100))
    raise ValueError('San diapazonnan sırtta: {}'.format(n))

# Funkciyanı test qılıw
print(convert_number_to_words(10000))