import unittest, ddt
from Unit_tools.DDT_xlsx.excel_red import get_data_from_excel
@ddt.ddt
class test_login(unittest.TestCase):
    def setUp(self):
        ...

    @ddt.data(*get_data_from_excel('../Unit_tools/DDT_xlsx/case.xlsx'))
    def subTest(self,data):
        ip = data['ip']
        interfase = data['interfase']
        headers = data['headers']
        datas = data['data']
        # print(data['ip'], data['interfase'], data['headers'], data['data'])
        print(ip, interfase, headers, datas)
        print("ddddddddddddddddd")
        ...

    def tearDown(self):
        ...

if __name__ == '__main__':
    unittest.main()