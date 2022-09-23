import unittest
from main import get_doc_owner_name, check_document_existance, delete_doc, add_new_doc
from parameterized import parameterized


class TestFunction(unittest.TestCase):
    @parameterized.expand(
        [
            (145, False),
            ('nffn', False),
            ('2207 876234', True),
            ('11-2', True),
            ('10006', True)
        ]
    )
    def test_check_document_existance(self, doc, result):
        function_result = check_document_existance(doc)
        self.assertEqual(function_result, result)

    @parameterized.expand(
        [
            ("10006", "Аристарх Павлов"),
            ("2207 876234", "Василий Гупкин")
        ]
    )
    def test_get_doc_owner_name(self, name, result):
        function_result = get_doc_owner_name(name)
        self.assertEqual(function_result, result)

    @parameterized.expand(
        [
            [("10006", True), None],
            [("11-2", True), None],
            [('2207 876234', True), None]
        ]
    )
    def test_delete_doc(self, docs, result):
        function_result = delete_doc(docs)
        self.assertEqual(function_result, result)

    @parameterized.expand(
        [
            ["passport", "3123 963741", "Иван Иванов", "4", "4"],
            ["invoice", "58745", "Петр Петров", "5", "5"],
            ["insurance", "365-876", "Денис Сидоров", "6", "6"]
        ]
    )
    def test_add_new_doc(self, doc, number, name, shelf, result):
        function_result = add_new_doc(doc, number, name, shelf)
        self.assertEqual(function_result, result)