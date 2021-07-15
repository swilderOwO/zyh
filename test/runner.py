from Pageobject.SearcH import Searchpage
from Page.Base import base
import unittest
from HTMLTestRunner import HTMLTestRunner
#HTMLTestRunner用来生成HTML格式的测试报告
import time
import os
from Page import email

class CRM(unittest.TestCase):
    def run_crm(self):
        run=Searchpage()
        run.add()       
if __name__ == '__main__':
    time.sleep(1)
    # 测试套件，构建测试集
    suite = unittest.TestSuite()
    suite.addTest(CRM('run_crm'))
    # 我们要新建一个用于保存我们测试结果的文件，html
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    print(now)
    # 定义文件的名字
    filename = 'C:/Users/Administrator/eclipse-workspace/T252/test/baogao/' + now + "_result.html"
    print(filename)
    file = open(filename, "wb")
    # 执行我们的报告写入
    runner = HTMLTestRunner(stream=file, title="crm_员工添加测试报告", description="用例执行情况:")
    # stream：是指定测试报告文件
    # title：指定报告的标题
    # description:指定报告的副标题
    # 执行我们测试用例
    runner.run(suite)
    time.sleep(3)
    # print(file.closed)
    # 要进行关闭
    file.close()
    print(file.closed)
# 发送邮件
a = os.listdir('C:/Users/Administrator/eclipse-workspace/T252/test/baogao/')
print(a)
dizhi = 'C:/Users/Administrator/eclipse-workspace/T252/test/baogao/' + a[-1]
print(dizhi)
email.send_mail(dizhi)