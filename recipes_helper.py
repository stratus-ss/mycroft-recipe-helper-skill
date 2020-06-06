cups_ml_constant_number = 0.0042268
cups_litres_constant_number = 4.2268
pints_ml_constant_number = 0.0021134
pints_litres_constant_number = 2.1134
fl_oz_ml_constant_number = 0.033814
fl_oz_litres_constant_number = 33.814
grams_oz_constant_number = 0.035274
grams_lbs_constant_number = 0.0022046

def convert_ml_to_litres(number_of_ml):
    return number_of_ml * 1000

def convert_cups_to_ml(number_of_cups):
    return number_of_cups / cups_ml_constant_number

def convert_cups_to_litres(number_of_cups):
    return number_of_cups / cups_litres_constant_number

def convert_ml_to_cups(number_of_ml):
    return number_of_ml * cups_ml_constant_number

def convert_litres_to_cups(number_of_litres):
    return number_of_litres * cups_litres_constant_number

def convert_pints_to_ml(number_of_pints):
    return number_of_pints / pints_ml_constant_number

def convert_pints_to_litres(number_of_pints):
    return number_of_pints / pints_litres_constant_number

def convert_ml_to_pints(number_of_ml):
    return number_of_ml * pints_ml_constant_number

def convert_litres_to_pints(number_of_litres):
    return number_of_litres * pints_litres_constant_number

def convert_fl_oz_to_ml(number_of_fl_oz):
    return number_of_fl_oz / fl_oz_ml_constant_number

def convert_fl_oz_to_litres(number_of_fl_oz):
    return number_of_fl_oz / fl_oz_litres_constant_number

def convert_ml_to_fl_oz(number_of_ml):
    return number_of_ml * fl_oz_ml_constant_number

def convert_litres_to_fl_oz(number_of_litres):
    return number_of_litres * fl_oz_litres_constant_number

def convert_oz_to_grams(number_of_oz):
    return number_of_oz / grams_oz_constant_number

def convert_lbs_to_grams(number_of_lbs):
    return number_of_lbs / grams_lbs_constant_number

def convert_grams_to_oz(number_of_grams):
    return number_of_grams * grams_oz_constant_number

def convert_grams_to_lbs(number_of_grams):
    return number_of_grams * grams_lbs_constant_number

def convert_cel_to_fahr(celcius):
    return (celcius * 1.8) + 32

def convert_fahr_to_cel(fahrenheit):
    return (fahrenheit - 32) / 1.8


def butter_from_tablespoon_conversion(unit='grams', number_of_tablespoons):
    unit_of_measurement = units.lower()
    if unit_of_measurement == "grams":
        number_of_grams = number_of_tablespoons * 14.19
        return number_of_grams
    if unit_of_measurement == "ounces":
        number_of_oz = number_of_tablespoons * 0.50
        return number_of_oz
    if unit_of_measurement == "lbs" of unit_of_measurement == "pounds":
        number_of_lbs = number_of_tablespoons * 0.03
        return number_of_lbs

def butter_from_teaspoon_conversion(unit='grams', number_of_teaspoons):
    unit_of_measurement = units.lower()
    if unit_of_measurement == "grams":
        number_of_grams = number_of_teaspoons * 4.73
        return number_of_grams
    if unit_of_measurement == "ounces":
        number_of_oz = number_of_teaspoons * 0.17
        return number_of_oz
    if unit_of_measurement == "lbs" of unit_of_measurement == "pounds":
        number_of_lbs = number_of_teaspoons * 0.01
        return number_of_lbs

def butter_from_cups_conversion(unit='grams', number_of_cups):
    unit_of_measurement = units.lower()
    if unit_of_measurement == "grams":
        number_of_grams = number_of_cups * 227
        return number_of_grams
    if unit_of_measurement == "ounces":
        number_of_oz = number_of_cups * 8.01
        return number_of_oz
    if unit_of_measurement == "lbs" of unit_of_measurement == "pounds":
        number_of_lbs = number_of_cups * 0.50
        return number_of_lbs




