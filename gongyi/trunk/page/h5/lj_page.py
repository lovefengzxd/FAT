# -*- coding: utf-8 -*-
import re

from gongyi.trunk.driver.box_driver import boxDriver
from main_page import mainPage
from page_map import *


class ljPage(mainPage):
    def lj_donate_money(self, money=None, select=None):
        """
        乐捐捐款
        :param money:自定义金额捐款
        :param select: 直接选定金额捐款:默认金额
        :return:捐款浮层的金额
        """

        self.h5_driver.h5_scroll_To_Xpath(lj_proj_map('项目介绍'))
        self.h5_driver.h5_click_by_text('我要捐款')
        self.h5_driver.h5_click_by_text('我已知情，继续捐赠')
        if select == None and money != None:
            self.h5_driver.h5_type_text(lj_proj_map('自定金额'), str(money))
        elif select != None and money == None:
            self.h5_driver.h5_click_by_xp(lj_proj_map('默认金额' % select))
        else:
            raise TypeError('key error')
        self.h5_driver.h5_click_by_xp(lj_proj_map('确定'))
        return self.h5_driver.h5_get_text_by_xp(lj_proj_map('捐款浮层支付金额'))

    def get_proj_name(self):
        """
        获取项目名称
        :return:
        """
        return self.h5_driver.h5_get_text_by_xp(lj_proj_map('项目名称'))

    def err_box(self):
        if self.h5_driver.h5_isElementExist(lj_proj_map('支付错误提示')):
            return self.h5_driver.h5_get_text_by_xp(lj_proj_map('支付错误提示'))
        else:
            return False
    def big_money_tips(self):
        if self.h5_driver.h5_isElementExist(lj_proj_map('大金额支付提示')):
            return self.h5_driver.h5_get_text_by_xp(lj_proj_map('大金额支付提示'))
        else:
            return False

    def get_thanks_page_info(self):
        """
        获取感谢页信息
        :return:
        """
        thanks_page_nick = self.h5_driver.h5_get_text_by_xp(lj_thanks_map('昵称'))
        projname = self.h5_driver.h5_get_text_by_xp(lj_thanks_map('项目名称'))
        thanks_page_money = self.h5_driver.h5_get_text_by_xp(lj_thanks_map('本次捐助'))
        thanks_page_experience = self.h5_driver.h5_get_text_by_xp(lj_thanks_map('爱心经验'))
        thanks_page_projname = re.match(r'.*\[(.*)\]', projname, re.S).group(1)
        thanks_page_transcode = re.match(r'.*transcode=(\d*)&.*', self.h5_driver.h5_get_url()).group(1)
        return {'昵称': thanks_page_nick, '项目名称': thanks_page_projname, '本次捐助': thanks_page_money,
                '爱心经验': thanks_page_experience, '流水单号': thanks_page_transcode}


if __name__ == '__main__':
    h = boxDriver()
    # h.close_wx()
    # h.open_wx()
    # h.load_h5Driver()
    # a=input("asd")
    h.load_xcxDriver()
    # print a
