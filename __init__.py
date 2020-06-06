from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.skills.context import adds_context, removes_context
from mycroft import intent_file_handler
from mycroft.util.log import getLogger
from adapt.intent import IntentBuilder


class RecipeHelperSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.cups_ml_constant_number = 0.0042268
        self.cups_litres_constant_number = 4.2268
        self.pints_ml_constant_number = 0.0021134
        self.pints_litres_constant_number = 2.1134
        self.fl_oz_ml_constant_number = 0.033814
        self.fl_oz_litres_constant_number = 33.814
        self.grams_oz_constant_number = 0.035274
        self.grams_lbs_constant_number = 0.0022046
        self.convert_from_this_unit = ''
        self.convert_to_this_unit = ''
        self.number_of_new_units = ''

    @staticmethod
    def convert_ml_to_litres(number_of_ml):
        return round((number_of_ml / 1000), 1)

    def convert_cups_to_ml(self, number_of_cups):
        return round((number_of_cups / self.cups_ml_constant_number), 1)

    def convert_cups_to_litres(self, number_of_cups):
        return round((number_of_cups / self.cups_litres_constant_number), 1)

    def convert_ml_to_cups(self, number_of_ml):
        return round((number_of_ml * self.cups_ml_constant_number), 1)

    def convert_litres_to_cups(self, number_of_litres):
        return round((number_of_litres * self.cups_litres_constant_number), 1)

    def convert_pints_to_ml(self, number_of_pints):
        return round((number_of_pints / self.pints_ml_constant_number), 1)

    def convert_pints_to_litres(self, number_of_pints):
        return round((number_of_pints / self.pints_litres_constant_number), 1)

    def convert_ml_to_pints(self, number_of_ml):
        return round((number_of_ml * self.pints_ml_constant_number), 1)

    def convert_litres_to_pints(self, number_of_litres):
        return round((number_of_litres * self.pints_litres_constant_number), 1)

    def convert_fl_oz_to_ml(self, number_of_fl_oz):
        return round((number_of_fl_oz / self.fl_oz_ml_constant_number), 1)

    def convert_fl_oz_to_litres(self, number_of_fl_oz):
        return round((number_of_fl_oz / self.fl_oz_litres_constant_number), 1)

    def convert_ml_to_fl_oz(self, number_of_ml):
        number_of_fl_oz = round((number_of_ml * self.fl_oz_ml_constant_number), 1)
        print(number_of_fl_oz)
        return number_of_fl_oz

    def convert_litres_to_fl_oz(self, number_of_litres):
        return round((number_of_litres * self.fl_oz_litres_constant_number), 1)

    def convert_oz_to_grams(self, number_of_oz):
        return round((number_of_oz / self.grams_oz_constant_number), 1)

    @staticmethod
    def convert_oz_to_lbs(number_of_oz):
        return round((number_of_oz / 16), 1)

    def convert_lbs_to_grams(self, number_of_lbs):
        return round((number_of_lbs / self.grams_lbs_constant_number), 1)

    @staticmethod
    def convert_lbs_to_oz(number_of_lbs):
        return round((number_of_lbs * 16), 1)

    def convert_grams_to_oz(self, number_of_grams):
        return round((number_of_grams * self.grams_oz_constant_number), 1)

    def convert_grams_to_lbs(self, number_of_grams):
        return round((number_of_grams * self.grams_lbs_constant_number), 1)

    @staticmethod
    def convert_cel_to_fahr(celsius):
        return round(((celsius * 1.8) + 32), 1)

    @staticmethod
    def convert_fahr_to_cel(fahrenheit):
        return round(((fahrenheit - 32) / 1.8), 1)

    @staticmethod
    def butter_weight_from_tablespoon(unit='grams', number_of_tablespoons=1):
        unit_of_measurement = unit.lower()
        if unit_of_measurement == "grams":
            return number_of_tablespoons * 14.19
        if unit_of_measurement == "ounces":
            return number_of_tablespoons * 0.50
        if unit_of_measurement in ["lbs", "pounds"]:
            return number_of_tablespoons * 0.03

    @staticmethod
    def butter_weight_from_teaspoon(unit='grams', number_of_teaspoons=1):
        unit_of_measurement = unit.lower()
        if unit_of_measurement == "grams":
            return number_of_teaspoons * 4.73
        if unit_of_measurement == "ounces":
            return number_of_teaspoons * 0.17
        if unit_of_measurement in ["lbs", "pounds"]:
            return number_of_teaspoons * 0.01

    @staticmethod
    def butter_weight_from_cups(unit='grams', number_of_cups=1):
        unit_of_measurement = unit.lower()
        if unit_of_measurement == "grams":
            return number_of_cups * 227
        if unit_of_measurement == "ounces":
            return number_of_cups * 8.01
        if unit_of_measurement in ["lbs", "pounds"]:
            return number_of_cups * 0.50

    def get_converted_units(self):
        return int(self.convert_from_this_unit.split()[0])

    def speak_conversion_weight(self):
        sentence = "%s weighs %s %s" % (self.convert_from_this_unit, self.number_of_new_units,
                                        self.convert_to_this_unit)
        self.speak(sentence)

    def speak_conversion_generic(self):
        sentence = "%s is %s %s" % (self.convert_from_this_unit, self.number_of_new_units,
                                        self.convert_to_this_unit)
        self.speak(sentence)

    @intent_file_handler("convert.butter.intent")
    def convert_butter(self, message):
        self.convert_from_this_unit = message.data.get('oldunit')
        self.convert_to_this_unit = message.data.get('newunit')
        if "butter" in message.data['utterance']:
            if "teaspoon" in self.convert_from_this_unit:
                self.number_of_new_units = self.butter_weight_from_teaspoon(unit=self.convert_to_this_unit,
                                                                            number_of_teaspoons=self.get_converted_units())
            elif "tablespoon" in message.data['utterance']:
                self.number_of_new_units = self.butter_weight_from_tablespoon(unit=self.convert_to_this_unit,
                                                                              number_of_tablespoons=self.get_converted_units())
            elif "cups" in message.data['utterance']:
                self.number_of_new_units = self.butter_weight_from_cups(unit=self.convert_to_this_unit,
                                                                        number_of_cups=self.get_converted_units())
            self.speak_conversion_weight()

    @intent_file_handler("convert.units.intent")
    def convert_units(self, message):
        self.convert_from_this_unit = message.data.get('oldunit')
        self.convert_to_this_unit = message.data.get('newunit')
        number_of_units_to_convert = self.get_converted_units()
        if "milliliter" in self.convert_from_this_unit or "ml" in self.convert_from_this_unit:
            if "liter" in self.convert_to_this_unit:
                self.number_of_new_units = self.convert_ml_to_litres(number_of_units_to_convert)
            elif "cup" in self.convert_to_this_unit:
                self.number_of_new_units = self.convert_ml_to_cups(number_of_units_to_convert)
            elif "pint" in self.convert_to_this_unit:
                self.number_of_new_units = self.convert_ml_to_pints(number_of_units_to_convert)
            elif "fluid ounce" in self.convert_to_this_unit:
                self.number_of_new_units = self.convert_ml_to_fl_oz(number_of_units_to_convert)
            else:
                exit()
        elif "gram" in self.convert_from_this_unit:
            if "ounce" in self.convert_to_this_unit:
                self.number_of_new_units = self.convert_grams_to_oz(number_of_units_to_convert)
            elif "lbs" in self.convert_to_this_unit or "pounds" in self.convert_to_this_unit:
                self.number_of_new_units = self.convert_grams_to_lbs(number_of_units_to_convert)
            else:
                exit()
        elif "liter" in self.convert_from_this_unit:
            if "cup" in self.convert_to_this_unit:
                self.number_of_new_units = self.convert_litres_to_cups(number_of_units_to_convert)
            elif "pints" in self.convert_to_this_unit:
                self.number_of_new_units = self.convert_litres_to_pints(number_of_units_to_convert)
            elif "fluid ounce" in self.convert_to_this_unit:
                self.number_of_new_units = self.convert_litres_to_fl_oz(number_of_units_to_convert)
            else:
                exit()
        elif "pounds" in self.convert_from_this_unit or "lbs" in self.convert_from_this_unit:
            if "ounce" in self.convert_to_this_unit:
                self.number_of_new_units = self.convert_lbs_to_oz(number_of_units_to_convert)
            elif "gram" in self.convert_to_this_unit:
                self.number_of_new_units = self.convert_lbs_to_grams(number_of_units_to_convert)
            else:
                exit()
        elif "cup" in self.convert_from_this_unit:
            if "milliliter" in self.convert_to_this_unit:
                self.number_of_new_units = self.convert_cups_to_ml(number_of_units_to_convert)
            elif self.convert_to_this_unit.startswith("liter"):
                self.number_of_new_units = self.convert_cups_to_litres(number_of_units_to_convert)
            else:
                exit()
        elif "pint" in self.convert_from_this_unit:
            if self.convert_to_this_unit.startswith("milliliter"):
                self.number_of_new_units = self.convert_pints_to_ml(number_of_units_to_convert)
            elif self.convert_to_this_unit.startswith("liter"):
                self.number_of_new_units = self.convert_pints_to_litres(number_of_units_to_convert)
            else:
                exit()
        elif "fluid" in self.convert_from_this_unit:
            if self.convert_to_this_unit.startswith("milliliter"):
                self.number_of_new_units = self.convert_fl_oz_to_ml(number_of_units_to_convert)
            elif self.convert_to_this_unit.startswith("liter"):
                self.number_of_new_units = self.convert_fl_oz_to_litres(number_of_units_to_convert)
            else:
                exit()
        elif "ounce" in self.convert_from_this_unit:
            if self.convert_to_this_unit.startswith("pound") or self.convert_to_this_unit.startswith("lbs"):
                self.number_of_new_units = self.convert_oz_to_lbs(number_of_units_to_convert)
            elif self.convert_to_this_unit.startswith("gram"):
                self.number_of_new_units = self.convert_oz_to_grams(number_of_units_to_convert)
            else:
                exit()
        elif "celsius" in self.convert_from_this_unit:
            self.number_of_new_units = self.convert_cel_to_fahr(number_of_units_to_convert)
        elif "fahrenheit" in self.convert_from_this_unit:
            self.number_of_new_units = self.convert_fahr_to_cel(number_of_units_to_convert)
        self.speak_conversion_generic()

    def stop(self):
        exit()


def create_skill():
    return RecipeHelperSkill()