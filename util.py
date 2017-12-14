from datetime import datetime
from werkzeug.routing import BaseConverter, ValidationError


class DateConverter(BaseConverter):
    """Extracts a ISO8601 date from the path and validates it."""

    regex = r'\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        try:
            return datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise ValidationError()

    def to_url(self, value):
        return value.strftime('%Y-%m-%d')


class ListStringConverter(BaseConverter):

    def to_python(self, value):
        try:
            return value.split('-')
        except ValueError:
            raise ValidationError()

    def to_url(self, value):
        pass

class ListIntConverter(BaseConverter):

    def to_python(self, value):
        try:
            return value.split('-')
        except ValueError:
            raise ValidationError()

    def to_url(self, value):
        pass


class ListofRoutesConverter(BaseConverter):

    def to_python(self, value):
        response = []
        
        try:

            comma =  value.split(',')
            ultElem = comma[-1]
            for elem in comma:
                code_elem = []
                code = elem.split('-')
                code_elem.append(str(code[0]))
                code_elem.append(str(code[1]))
                response.append(code_elem)

               
            return response
        except ValueError:
            raise ValidationError()

    def to_url(self, value):
        pass