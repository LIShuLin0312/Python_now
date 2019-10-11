import json
import os
import random
import re
import time
import jieba
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import subprocess
from APP_UA import APP_UA
from multiprocessing import Pool
from selenium.webdriver import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from gjc import gjc

# from runAdmin import runAdmin
# import pyautogui

# with open("C:\\Users\\Administrator\\Desktop\\gjc.txt",'r') as f:
#   m = f.read()
#  names = m.split("\n")
names = gjc


class Bai_du_seo():
    def __init__(self):
        Options = webdriver.ChromeOptions()
        Options.add_experimental_option('w3c', False)
        WIDTH = 360  # 宽度ßßß
        HEIGHT = 720  # 高度
        PIXEL_RATIO = 3.0  # 分辨率
        ua = random.choice(APP_UA)
        # print(ua)
        mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO},
                           "userAgent": ua}
        time.sleep(random.randint(1, 6))
        # self.ip = get_ip()
        self.ip = "127.0.0.1:8888"
        # print("当前代理IP：",ip)
        Options.add_argument('user-agent={}'.format(random.choice(APP_UA)))
        # Options.add_argument("--proxy-server=http://{}".format(ip))
        Options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以开发者状态运行
        Options.add_argument('--disable-gpu')
        Options.add_argument('--hide-scrollbars')  # 隐藏滚动条
        # Options.add_argument('--headless')  # 无头模式
        Options.add_argument('--incognito')  # 无痕模式
        Options.add_argument('--disable-infobars')  # 禁止显示自动化窗口
        Options.add_argument('--lang=zh-cn')  # 设置成中文模式
        Options.add_argument('lang=zh_CN.UTF-8"')  # 更换头部
        Options.add_argument('x-forwarded-for=201.33.33.44,220.166.229.142"')  # 更换头部
        Options.add_argument("-lang=zh-CN,zh;q=0.8")
        Options.add_experimental_option('mobileEmulation', mobileEmulation)
        prefs = {
            'profile.default_content_setting_values':
                {
                    'notifications': 2
                }
        }
        Options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(options=Options)
        self.driver.implicitly_wait(20)
        # self.driver.set_window_rect(x=random.choice(0,1000),y=random.choice(0,500),height=760,width=320)
        self.driver.set_window_size(random.randint(280, 420), random.randint(640, 960))
        # self.driver.set_window_position(x=random.choice(0,1000),y=0)
        # print("开始进入手机模式")
        # self.driver.implicitly_wait(5)
        # right_click = self.driver.find_element_by_id("hplogo")
        # right_click = self.driver.find_element_by_id("icon")
        # ActionChains(self.driver).context_click(right_click).perform()
        # self.driver.get("http://www.atool9.com/useragent.php")
        # self.driver.get("https://m.baidu.com")
        # time.sleep(999)
        # pyautogui.typewrite(['f12'])
        # time.sleep(30)
        # pyautogui.hotkey('ctrl', 'shift', 'm')
        # print("手机模式")
        time.sleep(2)

        self.driver.execute_script("""
                window.navigator.chrome = {
                    runtime: {},
                    // etc.
                  };""")
        self.driver.execute_script("""function touchStart(event) {
                          this.delta = {};
                          this.delta.x = event.touches[100].pageX;
                          this.delta.y = event.touches[-400].pageY;
                          this.delta.time = new Date().getTime();
                    }""")
        self.driver.execute_script("""
                const originalQuery = window.navigator.permissions.query;
                  return window.navigator.permissions.query = (parameters) => (
                    parameters.name === 'notifications' ?
                      Promise.resolve({ state: Notification.permission }) :
                      originalQuery(parameters)
                  );""")
        self.driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5], });")
        self.driver.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['zh-CN', 'zh']});")

    def kill_server(self, _port):
        p = os.popen('netstat -aon|findstr "{}"'.format(_port))
        p2 = p.read()

    def get_ip(self):
        ip_url = "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=100017&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4"
        ip = requests.get(ip_url).text
        print(ip)
        for i in range(9):
            if "再试" in str(ip):
                time.sleep(random.randint(1, 4))
                ip = requests.get(ip_url, timeout=5).text
            # 如果没有在白名单，就添加白名单
            elif "请添加白名单" in str(ip):
                self_ip = re.compile('"请添加白名单(.*?)","', re.S).findall(str(ip))[0]
                print("白名单添加中，本机IP：", self_ip)
                try:
                    x = requests.get(
                        "http://web.http.cnapi.cc/index/index/save_white?neek=79185&appkey=7b4bb8a059ff41c8f6782f11e73bff30&white={}".format(
                            self_ip))
                    print(x.text)
                except Exception as f:
                    print("白名单添加错误》》》", f)
                time.sleep(1)
                ip = requests.get(ip_url, timeout=5).text
            else:
                return ip.strip()

    def inst(self, name1, y, ip):
        with open("C:\\Users\\Administrator\\Desktop\\pintai6日志.log", 'a', encoding='utf-8') as f:
            f.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            f.write(name1)
            f.write(" | ")
            f.write(y)
            f.write("当前IP：")
            f.write(str(ip))
            f.write("\n")
            print("点击成功：=================》：", y)
            time.sleep(5)

    def i_next(self):
        a_s = self.driver.find_elements_by_xpath("//a")
        el = random.choice(a_s)
        el.click()
        time.sleep(random.randint(30, 60))

    def show_click(self, name1, ip):
        ciss = self.driver.find_elements_by_xpath('//div[@class="c-showurl c-line-clamp1"]')
        for i in ciss:
            y = i.get_attribute('textContent')
            if "广告" not in y:
                if "www.ihuashi.cn" in y or "m.ihuashi.cn" in y:
                    y = i.get_attribute('textContent')
                    el = i.find_element_by_xpath("./..")
                    el.click()
                    # self.driver.execute_script("arguments[0].click();",el)
                    self.inst(name1, y, ip)
                    for i in range(4):
                        self.i_next()

    def run_web(self):
        try:
            self.driver.get("https://m.baidu.com/")
            name1 = random.choice(names)
            print(name1)
            name = list(jieba.cut(name1))

            for i in name:
                self.driver.find_element_by_id("index-kw").send_keys(i)
                time.sleep(random.randint(0, 2))
            self.driver.find_element_by_id("index-kw").submit()
            for i in range(5):
                try:
                    self.driver.switch_to.alert.accept()
                except:
                    pass
                time.sleep(1)
            # 滑动

            y1 = 0
            Action = TouchActions(self.driver)
            for i in range(random.randint(2, 4)):
                x1 = int(self.driver.get_window_size()['width'] * random.randint(30, 70) / 100)
                y = int(self.driver.get_window_size()['height'] * random.randint(15, 35) / 100)
                y1 += y
                print("第{}次滑动".format(i))
                Action.scroll(xoffset=x1, yoffset=y1).perform()
                # self.driver.execute_script("window.scrollTo({},{})".format(x1,y1))
                time.sleep(random.randint(1, 4))
            for i in range(1, 4):
                if i == 1:
                    self.show_click(self.driver, name1)
                else:
                    self.driver.find_element_by_xpath(
                        "//span[contains(text(),'加载更多')]|//p[contains(text(),'下一页')]").click()
                    time.sleep(3)
                    self.show_click(self.driver, name1)

        except Exception as f:
            print(f)
        finally:
            try:
                self.driver.delete_all_cookies()
                self.driver.execute_script("window.localStorage.clear();")
                self.driver.execute_script("window.sessionStorage.clear();")
                self.driver.quit()
            except Exception as f:
                pass
            else:
                print("清除Cookies与缓存成功")


def run(i):
    # print(i)
    seo = Bai_du_seo()
    seo.run_web()


if __name__ == '__main__':
    pools = Pool()
    while True:
        try:
            for i in range(1):
                pools.apply_async(run, args=(i,))
            pools.close()
            pools.join()
        except:
            pass
