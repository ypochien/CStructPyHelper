import unittest

from CStructPyHelper import CStructPyHelper


class test_CStructPyHelperCase(unittest.TestCase):
    def test_give_c_struct_should_retun_struct_name(self):
        data='''F_OS_SEND_FILLDATA
{
    char account[14];
    int ord_match_qty;
    int ord_match_amt;
    int ord_match_avg_prc;
    int update_qty;
}
'''
        actor = CStructPyHelper(data)
        actual = actor.name()
        expected = 'F_OS_SEND_FILLDATA'
        self.assertEqual(expected,actual)




if __name__ == '__main__':
    unittest.main()
