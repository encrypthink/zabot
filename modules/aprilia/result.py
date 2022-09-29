from datetime import date, datetime, timedelta
from time import strftime

class Result:
    def result_all(self, columns, raw):
        result: list() = []

        i = 0
        for row in raw:
            in_row: dict() = {}
            j = 0
            for val in row:    
                in_row[columns[j]] = self.validate_type(val)
                j = j+1

            result.append(in_row)
            i = i+1

        return result

    def result_row(self, columns, raw):
        result: dict() = {}
        i = 0

        for val in raw:
            result[columns[i]] = self.validate_type(val)
            i = i+1

        return result

    def result_one(self, raw):
        return raw[0]

    def validate_type(self, value) -> any:
        result = None
        
        if type(value) == datetime:
            result = value.strftime("%Y-%m-%d %H:%M:%S")
        elif type(value) == date:
            result = value.strftime("%Y-%m-%d")
        elif type(value) == timedelta:
            result = str(value)
        else:
            result = value

        return result