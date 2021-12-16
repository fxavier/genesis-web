from datetime import date


class Helpers:

    @staticmethod
    def formatDate(date):
        if date is None or date == "":
            return date(1900, 1, 1)
        else:
            return date
