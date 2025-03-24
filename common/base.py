from common import *


class base():

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.timeout = 15
        self.t = 0.5

    # 元素定位
    def findElement(self, locator):
        # ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x:x.find_element(*locator))
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
        # print("定位到的元素为------:"+str(locator))
        return ele

    # 元素判断
    def findElementNew(self, locator):
        '''
        定位到元素，返回元素对象，没有定位到timout异常
        '''
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
        return ele

    # 滑动登录图片
    def move_by_offset(self, locator):
        # 获取元素
        els = self.findElement(locator)
        # 创建ActionChains对象
        action = ActionChains(self.driver)
        # 模拟鼠标按下滑块
        action.click_and_hold(els)
        # 移动鼠标到指定距离向右滑动200个单位
        action.move_by_offset(200, 0)
        # 释放鼠标
        action.release()
        # 执行ActionChins操作
        action.perform()

    #  判断当前页面的title是否完全等于（==）预期字符串，返回布尔值
    def is_title(self, _title):
        '''
        返回bool值
        :param _title:
        :return:
        '''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    # 判断当前页面的title是否包含预期字符串，返回布尔值
    def is_title_contains(self, _title):
        '''
        返回bool值
        :param _title:
        :return:
        '''
        try:
            result= WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    # 判断某个元素中的text是否 包含 了预期的字符串
    def is_text_in_element(self, locator, _text):
       try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
            return result
       except:
            return False

    # 判断某个元素中的value属性是否 包含 了预期的字符串
    def is_value_in_element(self, locator, _value):
        '''空字符串返回False'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t)\
                .until(EC.text_to_be_present_in_element_value(locator, _value))
            return result
        except:
            return False

    # 判断页面上是否存在alert
    def is_alert(self):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    # 输入内容
    def sendKeys(self, locator, text):
        ele =self.findElement(locator)
        ele.send_keys(text)
        time.sleep(1)
        # print("元素定位，输入框输入的内容为："+str(text))

    #  输入内容
    def sendKeys_clear(self, locator, text):
        ele =self.findElement(locator)
        ele.clear()
        ele.send_keys(text)
        time.sleep(1)
        # print("元素定位，输入框输入的内容为："+str(text))

    # 点击事件
    def click(self, locator):
        ele = self.findElement(locator)
        time.sleep(0.5)
        # print("点击元素： "+str(locator))
        ele.click()

    # 清空输入框
    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()

    # 判断元素是否存在
    def isElementExist(self, locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    # 判断元素是否存在
    def isElementExist2(self, locator):
        eles = self.findElement(locator)
        n = len(eles)
        if n==0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到了多个元素")
            return True

    # 鼠标悬停操作
    def move_to_element(self, locator):
        '''鼠标悬停操作'''
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def js_scroll_end(self):
        '''滚动到底部'''
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def js_focus(self, loctor):
        '''滚动到元素出现位置,聚焦元素'''
        target = self.findElement(loctor)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''回到顶部'''
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)

    def fefresh(self):
        '''刷新'''
        self.driver.refresh()
        time.sleep(2)

    def maximize_window(self):
        ''' 最大化页面'''
        self.driver.maximize_window()

    # 关闭浏览器
    def close(self):
        self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()

    def close_driver(self):
        self.driver.close()
        self.driver.quit()

    def clear_cookie(self):
        self.driver.delete_all_cookies()

    def alert(self):
        return self.driver.switch_to.alert

    def getImage(self, imgPath):
        '''截取图片,并保存在images文件夹'''
        time.sleep(0.5)
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath = os.path.join(imgPath, '%s.png' % str(timestrmap))
        self.driver.save_screenshot(imgPath)
        print('screenshot:', timestrmap, '.png')

    # def get_value(self,locator):
    #     ele=self.findElement(locator)
    #     n=ele.text
    #     return n

# title_is： 判断当前页面的title是否完全等于（==）预期字符串，返回布尔值
# title_contains : 判断当前页面的title是否包含预期字符串，返回布尔值
# presence_of_element_located : 判断某个元素是否被加到了dom树里，并不代表该元素一定可见
# visibility_of_element_located : 判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
# visibility_of : 跟上面的方法做一样的事情，只是上面的方法要传入locator，这个方法直接传定位到的element就好了
# presence_of_all_elements_located : 判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是'column-md-3'，
# 那么只要有1个元素存在，这个方法就返回True
# text_to_be_present_in_element : 判断某个元素中的text是否 包含 了预期的字符串
# text_to_be_present_in_element_value : 判断某个元素中的value属性是否 包含 了预期的字符串
# frame_to_be_available_and_switch_to_it : 判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
# invisibility_of_element_located : 判断某个元素中是否不存在于dom树或不可见
# element_to_be_clickable : 判断某个元素中是否可见并且是enable的，这样的话才叫clickable
# staleness_of : 等某个元素从dom树中移除，注意，这个方法也是返回True或False
# element_to_be_selected : 判断某个元素是否被选中了,一般用在select下拉列表
# element_selection_state_to_be : 判断某个元素的选中状态是否符合预期
# element_located_selection_state_to_be : 跟上面的方法作用一样，只是上面的方法传入定位到的element，而这个方法传入locator
# alert_is_present : 判断页面上是否存在alert

if __name__ == "__main__":
    ...
