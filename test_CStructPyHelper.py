import unittest

from CStructPyHelper import CStructPyHelper


class test_CStructPyHelperCase(unittest.TestCase):
    def setUp(self):
        self.data = '''F_OS_SEND_FILLDATA
{
    char account[14];
    int ord_match_qty;
    unsigned char ord_match_amt [5 ];
    int ord_match_avg_prc;
    unsigned char update_qty;
    char first_login;
}'''

    def test_give_c_struct_should_retun_struct_name(self):
        actor = CStructPyHelper(self.data)
        actual = actor.name()
        expected = 'F_OS_SEND_FILLDATA'
        self.assertEqual(expected, actual)

    def test_struct_memeber_numbers_are_equle(self):
        actor = CStructPyHelper(self.data)
        actual = len(actor.row_contents())
        expected = 6
        self.assertEqual(expected, actual)

    def test_struct_member_should_pure_data(self):
        actor = CStructPyHelper(self.data)
        actual = actor.row_contents()
        expected = 'char account[14]'
        self.assertEqual(expected, actual[0])
        expected = 'int ord_match_qty'
        self.assertEqual(expected, actual[1])
        expected = 'unsigned char ord_match_amt [5 ]'
        self.assertEqual(expected, actual[2])

    def test_get_struct_member_content_size(self):
        actor = CStructPyHelper(self.data)
        text_members = actor.row_contents()
        actual = actor.get_size(text_members[0])
        expected = 14
        self.assertEqual(expected, actual)
        actual = actor.get_size(text_members[1])
        expected = ''
        self.assertEqual(expected, actual)
        actual = actor.get_size(text_members[2])
        expected = 5
        self.assertEqual(expected, actual)

    def test_get_struct_member_content_type(self):
        actor = CStructPyHelper(self.data)
        text_members = actor.row_contents()
        actual = actor.get_type(text_members[0])
        expected = 'char[]'
        self.assertEqual(expected, actual)
        actual = actor.get_type(text_members[1])
        expected = 'int'
        self.assertEqual(expected, actual)
        actual = actor.get_type(text_members[2])
        expected = 'unsigned char'
        self.assertEqual(expected, actual)
        actual = actor.get_type(text_members[5])
        expected = 'char'
        self.assertEqual(expected, actual)

    def test_get_struct_member_content_name(self):
        actor = CStructPyHelper(self.data)
        text_members = actor.row_contents()
        actual = actor.get_name(text_members[0])
        expected = 'account'
        self.assertEqual(expected, actual)
        actual = actor.get_name(text_members[1])
        expected = 'ord_match_qty'
        self.assertEqual(expected, actual)
        actual = actor.get_name(text_members[2])
        expected = 'ord_match_amt'
        self.assertEqual(expected, actual)

    def test_input_one_row_content_shoud_be_return_py_struct_fmt(self):
        actor = CStructPyHelper(self.data)
        text_members = actor.row_contents()
        actual = actor.get_struct_fmt(text_members[0])
        expected = '14s'
        self.assertEqual(expected, actual)
        actual = actor.get_struct_fmt(text_members[1])
        expected = 'i'
        self.assertEqual(expected, actual)
        actual = actor.get_struct_fmt(text_members[2])
        expected = '5B'
        self.assertEqual(expected, actual)
        actual = actor.get_struct_fmt(text_members[3])
        expected = 'i'
        self.assertEqual(expected, actual)
        actual = actor.get_struct_fmt(text_members[4])
        expected = 'B'
        self.assertEqual(expected, actual)
        actual = actor.get_struct_fmt(text_members[5])
        expected = 'c'
        self.assertEqual(expected, actual)

    def test_data_to_full_py_struct_fmt(self):
        '''Get Python Struct module format.'''
        actor = CStructPyHelper(self.data)
        actual = actor.get_full_fmt()
        expected = '14si5BiBc'
        self.assertEqual(expected, actual)

    def test_data_to_full_member_name_list(self):
        '''Get struct member name list.'''
        actor = CStructPyHelper(self.data)
        actual = actor.get_member_list()
        expected = ['account', 'ord_match_qty', 'ord_match_amt', 'ord_match_avg_prc', 'update_qty', 'first_login']
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
