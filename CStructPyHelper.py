# coding=UTF-8
# __author__ == ypochien@gmail.com

class CStructPyHelper(object):
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

    def __init__(self, data):
        self._raw_data = data

    def name(self):
        return self._raw_data.strip().split('\n')[0]

    def row_contents(self):
        self.row_contents = []
        pos_start = self._raw_data.find('{') + 1
        pos_end = self._raw_data.find('}')

        struct_member_content = self._raw_data[pos_start:pos_end]
        for row in struct_member_content.strip().split('\n'):
            row = row.strip()
            row_end = row.find(';')
            self.row_contents.append(row[:row_end])
        return self.row_contents

    def get_size(self, row_text):
        pos_start = row_text.find('[')
        if pos_start >= 0:
            pos_end = row_text.find(']')
            number_text = row_text[pos_start + 1:pos_end].strip()
            return int(number_text)

        return ''

    def get_type(self, row_text):
        content = CStructPyHelper.parse_pure_type_with_name(row_text)
        content_type = ' '.join(content.strip().split(' ')[:-1])
        if 'char' == content_type and '[' in row_text:
            content_type += '[]'
        return content_type

    def get_name(self, row_text):
        content = CStructPyHelper.parse_pure_type_with_name(row_text)
        return content.strip().split(' ')[-1]

    @staticmethod
    def parse_pure_type_with_name(row_text):
        pos_start = row_text.find('[')
        content = row_text
        if pos_start >= 0:
            content = row_text[:pos_start]
        return content

    def get_struct_fmt(self, row_text):
        member_type = self.get_type(row_text)
        member_size = self.get_size(row_text)
        return '{}{}'.format(member_size, CStructPyHelper._struct_format_table[member_type])

    def get_full_fmt(self):
        text_members = self.row_contents()
        full_fmt = ''.join([self.get_struct_fmt(row_content) for row_content in text_members])
        return full_fmt

    def get_member_list(self):
        text_members = self.row_contents()
        name_list = [self.get_name(row_raw) for row_raw in text_members]
        return name_list
