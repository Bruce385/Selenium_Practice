class Page(object):
    '''页面基础类，用于所有页面的继承'''
    hf_url = 'https://www.hfpark.cn'

    def __init__(self, driver, base_url=hf_url, parent=None):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), '访问页面不正确：%s' % url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == self.base_url + self.url

    def script(self, src):
        return self.driver.execute_script(src)

    def switch_to_alert(self):
        return self.driver.switch_to_alert()
