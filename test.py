import unittest
from controller.config import *
import requests
from controller.Validator import *


class TestMain(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000/api/v1/"

    PAYLOAD_CREATE_CODE = {}
    PAYLOAD_UPDATE_CODE = {}
    max_limit = 0
    start_offset = 0
    max_icd_code = 7
    min_icd_code_len = 3
    validator = None
    icd_10_code = "A011238"

    def setUp(self):
        """called before testing a component"""

        self.PAYLOAD_CREATE_CODE = {
            "category_code": "A05", "diagnosis_code": "1238",
            "full_icd_code": "A051238", "abbreviated_description": "Comma-ind anal dop",
            "full_description": "Comma-induced anal retention",
            "category_title": "Malignant neoplasm of anus and anal canal",
            "icd_type": "ICD-10"}

        self.PAYLOAD_UPDATE_CODE = {
            "category_code": "A05", "diagnosis_code": "1238",
            "full_icd_code": "A051238", "abbreviated_description": "Comma-ind anal dialate",
            "full_description": "Comma-induced anal retention",
            "category_title": "Malignant neoplasm of anus and anal canal",
            "icd_type": "ICD-10"}

        self.validator = Validate()

        self.max_limit = 2
        min_icd_code_len = 3
        max_icd_code = 7
        pass

    def tearDown(self):
        pass

    def test_create_new_diagnose_code(self):
        response = requests.post("http://127.0.0.1:5000/api/v1/create", json=self.PAYLOAD_CREATE_CODE)
        self.assertEqual(response.status_code, 201, "Excepted 201")
        self.assertEqual(response.json()['status'], 'success', "Expecting success")
        pass

    def test_dummy_record(self):
        response = requests.get("http://127.0.0.1:5000/api/v1/test")
        self.assertEqual(response.status_code, 200, "expecting 200")
        self.assertEqual(response.json()['msg'], "Testing the Program")
        pass

    def test_update_new_diagnose_code(self):
        response = requests.put('http://127.0.0.1:5000/api/v1/update/2', json=self.PAYLOAD_UPDATE_CODE)
        self.assertEqual(response.status_code, 200, "expecting 200")
        self.assertEqual(response.json()['status'], "success", "Expecting success")
        pass

    def test_delete_record(self):
        response = requests.delete("http://127.0.0.1:5000/api/v1/delete/4")
        self.assertEqual(response.status_code, 200, "Expecting 200")
        self.assertEqual(response.json()['status'], "success", "Expecting Success")
        pass

    def test_list_codes(self):
        response = requests.get('http://127.0.0.1:5000/api/v1/list')
        self.assertEqual(response.status_code, 200, "Expecting 200")
        pass


    def test_fetch_single_record(self):
        response = requests.get("http://127.0.0.1:5000/api/v1/list/1")
        self.assertEqual(response.status_code, 200, "Expecting 200")
        self.assertEqual(response.json()['count'], 1, "Expecting 1")
        pass


    def test_valid_icd_code_length(self):
        response = self.validator.valid_code_length(self.icd_10_code,
                    self.min_icd_code_len, self.max_icd_code)
        self.assertTrue(response, "Expect True ")
        pass

    def test_valid_empty_field(self):
        response = self.validator.is_empty_field('A00023')
        self.assertTrue(response, "Expected True")
        pass

    if __name__ == '__main__':
        unittest.main()
