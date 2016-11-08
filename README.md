 # CStructPyHelper
Convert Python struct Format string from C Struct header.

struct in C / C++ like below:
```
F_OS_SEND_FILLDATA
{
    char account[14];
    int ord_match_qty;
    unsigned char ord_match_amt [5 ];
    int ord_match_avg_prc;
    unsigned char update_qty;
    char first_login;
}
```

using struct in Python:
```
account, ord_match, ord_match_amt, match_avg_prc, update_qty, first_login = struct.unpack('14si5BiBc' , data )
```

But Convert *HUGE* struct is too hard.

Then you can using this tools.
# Usage:
## ref test_CStructPyHelper.py 
```
struct_data_in_c = '''F_OS_SEND_FILLDATA
{
    char account[14];
    int ord_match_qty;
    unsigned char ord_match_amt [5 ];
    int ord_match_avg_prc;
    unsigned char update_qty;
    char first_login;
}'''
actor = CStructPyHelper(struct_data_in_c)
print actor.get_full_fmt()
print actor.get_member_list()
```
```
14si5BiBc
['account', 'ord_match_qty', 'ord_match_amt', 'ord_match_avg_prc', 'update_qty', 'first_login']
```

### python struct - https://docs.python.org/2/library/struct.html
