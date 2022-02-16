from marshmallow import ValidationError, fields
from pycpfcnpj import cpf

from alfred.tools.core import only_digits


class BRDocumentField(fields.String):
    def _deserialize(self, value, attr, data, **kwargs):
        value = super()._deserialize(value, attr, data, **kwargs)
        document = only_digits(value)
        valid_CPF = cpf.validate(value)

        if not valid_CPF:
            raise ValidationError(self.error_messages["document_error_msg"])

        return document

    def __init__(self, document_error_msg="CPF inválido", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages["document_error_msg"] = document_error_msg
