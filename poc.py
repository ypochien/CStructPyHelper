# coding=UTF-8
# __author__ == ypochien@gmail.com

src_struct = '''
F_OS_SEND_FILLDATA
{
    char account[14];
    int ord_match_qty;
    int ord_match_amt;
    int ord_match_avg_prc;
    int update_qty;
    int cancel_qty;
    char match_time[8];
    char mtype[1];               /* O : Oversea, I : Inside  */
    char firm[7];               /* Ex : F002000         */
    char actno[7];               /* Ex : 9108336         */
    char exh[3];               /* Ex : TIM         */
    char seqno[6];               /* Ex : Y35008          */
    char orddt[8];               /* YYYY/MM/DD           */
    char ordtm[6];               /* HHMMSS           */
    char ps[1];               /* B/S              */
    char comtype[1];               /* 0 : Future, 1 : Option   */
    char comno[10];               /* Ex : FIMTX, TXO      */
    char   comym[6];               /* YYYYMM           */
    int  stkprc;                         /* Ex : TXO05600F4->5600    */
    char callput[1];               /* Future:N, Option Call:C, Option Put:P */
    int     ordqty;                         /* */
    double  price1;                         /* Ex : 192.0           */
    int     price2;                         /* */
    int     price3;                         /* */
    char    ordtype[3];               /* 1:MKT/2:LMT/3:MIT/4:STP/CXL:/UPD:/UPL:/UPM*/
    char    dtrade[1];               /* " " */
    char    ordknd[3];               /* F : FOK, I : IOC, R : ROD    */
    char    session[2];               /* " " */
    char    opof[1];               /* " " */
    char    code[4];               /* */
    char    ordno[6];               /* */
    char    errmsg[52];               /* 60 -> 52   2012.04.13 ann */
    int     cnt;                            /* */
    char    type[1];               /* P : HTS, W : WTS, B : BTS    */
    char    process_fg[1];
    char    userid[10];
    int     multi_ord_no;
    char    acctgrpname[16];
    char    item_grpno[3];
    char    agent_id[6];                /*michael 20070104 added*/
    char bk_acnt[15];
    char fun_seq[6];
}
'''


class structHelper(object):
    _struct_format_table = {
        'pad byte': 'x',
        'char': 'c',
        'signed char': 'b',
        'unsigned char': 'B',
        'bool': '?',
        'BOOL': '?',
        'short': 'h',
        'unsigned short': 'H',
        'int': 'i',
        'unsigned int': 'I',
        'long': 'l',
        'unsigned long': 'L',
        'long long': 'q',
        'unsigned long long': 'Q',
        'float': 'f',
        'double': 'd',
        'char[]': 's',
        'void *': 'P'
    }
    
    def __init__(self, struct_header):
        self._raw = struct_header
        self._read()
        self.FMT = self.getFMT()
    
    def _read(self):
        self.ST_NAME = self._raw.split('{')[0].strip()
        self.st_list = []
        st_items = self._raw.split('{')[1].strip()
        st_items = [st_item for st_item in st_items.split('\n')[:-1]]  # char account     [14]; //OOXX
        for item in st_items[0:-1]:
            find_end = item.find(';')
            item = item[0:find_end].rstrip()  # char account[14 ]
            st_type = ' '.join(item.split(' ')[0:-1]).strip()  # char account     [14]; //OOXX
            st_name = item.split(' ')[-1]
            st_itemsize = ''
            idx = st_name.find("[")
            idx_e = st_name.find("]")
            if idx >= 0:
                print st_name
                st_itemsize = int(st_name[idx+1:idx_e].strip())
                st_itemname = st_name[:idx]
                st_name = st_itemname
            self.st_list.append((st_type, st_name, st_itemsize))
    
    def type_to_fmt(self, c_st_type):
        return self._struct_format_table[c_st_type]
    
    def getFMT(self):
        fmt = ['{}{}'.format(st_item[2], self._struct_format_table[st_item[0]]) for st_item in self.st_list]
        return ''.join(fmt)
    
    def getFiledName(self):
        return [st_item[1] for st_item in self.st_list]


sino_st = structHelper(src_struct)
print sino_st.ST_NAME, sino_st.FMT
print sino_st.getFiledName()
