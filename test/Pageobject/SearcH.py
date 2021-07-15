from Page.Base import base
from selenium.webdriver.common.by import By
import time
import pyautogui

# def find(self, *args):
#     try:
#         return self.driver.find_element(*args)
#     except:
#         print("定位失败")
class Searchpage(base):
      from selenium.webdriver.support.select import Select
      def add (self) :
        # 点击管理员且点击添加员工，然后切换到工作台
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name ('frame')[1])
        self.find (By.XPATH,'//*[@id="imgmenu4"]/table/tbody/tr/td[2]').click ()
        self.find (By.LINK_TEXT,'添加员工').click ()
        self.driver.switch_to.default_content ()
        self.driver.switch_to_frame(self.driver.find_elements_by_tag_name ('frame')[2])

        self.find (By.NAME,'userName').send_keys ('张三123')

        self.find (By.NAME,'userAge').send_keys ('25')

        sex = self.find (By.NAME,'userSex')
        sex.click ()
        time.sleep (1)
        self.Select(sex).select_by_index (1)
        sex.click ()
        userDiploma = self.find (By.NAME,'userDiploma')
        userDiploma.click ()
        time.sleep (1)
        self.Select(userDiploma).select_by_index (1)
        userDiploma.click ()
        departmentId = self.find (By.NAME,'departmentId')
        departmentId.click ()
        time.sleep(1)
        self.Select (departmentId).select_by_index (1)
        departmentId.click ()

        # 座机
        self.find (By.CSS_SELECTOR,'[valid = "isPhone"]').send_keys ('028-88888888')

        # 工资卡号
        self.find (By.CSS_SELECTOR,'[valid = "isNumber"]').send_keys ('6221546549873212589')

        # 身份证
        self.find (By.CSS_SELECTOR,'[valid = "isIdCard"]').send_keys ('51012219991111111X')

        # 添加人
        self.driver.implicitly_wait (3)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name ('frame')[0])
        person = self.find (By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table'
                                     '/tbody/tr/td[1]/table/tbody/tr/td[2]/div').text
        person1 = person.split ('：')
        self.driver.switch_to.default_content ()
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name ('frame')[2])
        self.find (By.NAME,'userAddman').send_keys (person1 [1])

        # 账号
        self.find (By.NAME,'userNum').send_keys ('admin123456')

        # 密码
        self.find (By.NAME,'userPw').send_keys ('123456')

        # 民族
        self.find (By.NAME,'userNation').send_keys ('汉族')

        # 婚姻
        isMarried = self.find (By.NAME,'isMarried')
        isMarried.click ()
        time.sleep (1)
        self.Select (isMarried).select_by_index (1)
        isMarried.click ()

        # 角色
        roleId = self.find (By.NAME,'roleId')
        roleId.click ()
        time.sleep (1)
        self.Select (roleId).select_by_index (0)
        roleId.click ()

        # 爱好
        self.find (By.NAME,'userIntest').send_keys ('打游戏')

        # 手机
        self.find (By.CSS_SELECTOR,'[valid = "regexp"]').send_keys ('18888888888')

        # 地址
        self.find (By.NAME,'userAddress').send_keys ('四川省成都市')

        # E_mail
        self.find (By.NAME,'userEmail').send_keys ('777777777@qq.com')

        # 添加按钮
        self.find (By.NAME,'submit').click ()

        # 获取提示框的文本
        time.sleep (2)
        notice = self.driver.switch_to.alert.text
        time.sleep (2)
        self.driver.switch_to.alert.accept ()
        self.driver.quit()

    