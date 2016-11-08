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
```
data = '''F_OS_SEND_FILLDATA
{
    char account[14];
    int ord_match_qty;
    unsigned char ord_match_amt [5 ];
    int ord_match_avg_prc;
    unsigned char update_qty;
    char first_login;
}'''
actor = CStructPyHelper(self.data)
print actor.get_full_fmt()
```
```
14si5BiBc
```
