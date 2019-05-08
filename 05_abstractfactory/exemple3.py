# From: Python 3 Object-Oriented Programming - Third Edition
# by Dusty Phillips
# Published by Packt Publishing, 2018

class FranceDateFormatter:
    def format_date(self, year, month, day):
        y, m, d = [str(x) for x in (year, month, day)]
        year = "20" + year if len(year) == 2 else year
        month = "0" + month if len(month) == 1 else month
        day = "0" + day if len(day) == 1 else day
        return f"{day}/{month}/{year}"


class USADateFormatter:
    def format_date(self, year, month, day):
        year, month, day = [str(x) for x in (year, month, day)]
        year = "20" + year if len(year) == 2 else year
        month = "0" + month if len(month) == 1 else month
        day = "0" + day if len(day) == 1 else day
        return f"{month}-{day}-{year}"


class FranceCurrencyFormatter:
    def format_currency(self, base, cents):
        base, cents = [str(x) for x in (base, cents)]
        if len(cents) == 0:
            cents = "00"
        elif len(cents) == 1:
            cents = "0" + cents

        digits = []
        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(" ")
            digits.append(c)
        base = "".join(reversed(digits))
        return f"{base}€{cents}"


class USACurrencyFormatter:
    def format_currency(self, base, cents):
        base, cents = [str(x) for x in (base, cents)]
        if len(cents) == 0:
            cents = "00"
        elif len(cents) == 1:
            cents = "0" + cents
        digits = []
        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(",")
            digits.append(c)
        base = "".join(reversed(digits))
        return f"${base}.{cents}"

class USAFormatterFactory:
    def create_date_formatter(self):
        return USADateFormatter()

    def create_currency_formatter(self):
        return USACurrencyFormatter()


class FranceFormatterFactory:
    def create_date_formatter(self):
        return FranceDateFormatter()

    def create_currency_formatter(self):
        return FranceCurrencyFormatter()

 

country_code = "FR"

factory_map = {
    "US": USAFormatterFactory, 
    "FR": FranceFormatterFactory
}

formatter_factory = factory_map.get(country_code)()