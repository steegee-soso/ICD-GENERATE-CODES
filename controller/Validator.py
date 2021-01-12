# Validate Modules
import re


class Validate:
    flag = True

    def __init__(self):
        pass

    def is_empty_field(self, field):
        if field.strip() == "":
            self.flag = False
        return self.flag

    def valid_icd_code(self, code):
        return bool(re.match('^[A-Za-z0-9]+$', code))
        pass

    def validate_diagnose_number(self, diagnose_num):
        return bool(re.match('^[0-9]+$', diagnose_num))
        pass

    def valid_code_length(self, code, min_len, max_len):
        if len(code.strip()) < min_len or len(code.strip()) > max_len:
            self.flag = False
        return self.flag
