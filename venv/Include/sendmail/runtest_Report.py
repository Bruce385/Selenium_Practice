import unittest
from HTMLTestRunner import HTMLTestRunner
import HTMLTestReportCN
import time
from mailtest import MailTest

# 定义测试用例的路径
test_dir = "./test_case"
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
# discover = unittest.defaultTestLoader.discover(".", pattern="Test*.py")

if __name__ == '__main__':
    report_dir = "./test_report"  # 定义存放报告的路径
    now = time.strftime("%y-%m-%d %H_%M_%S")  # 对报告的时间命名格式化
    report_name = report_dir + '/' + now + "result.html"  # 报告文件的完整路径

    # 打开文件，在报告文件写入测试结果
    with open(report_name, 'wb') as f:
        runner = HTMLTestReportCN.HTMLTestRunner(stream=f, title="测试报告" + "_Baidu", description="测试用例执行结果")
        runner.run(discover)  # 执行测试用例
    f.close()  # 保存后关闭文件

    MailTest(report_dir).send_mail()
