"""
    @Author: ImYrS Yang
    @Date: 2023/2/11
    @Copyright: ImYrS Yang
    @Description: 
"""

from typing import List

import requests


class Bot:

    def __init__(self, app_key, app_secret):
        self.app_key = app_key
        self.app_secret = app_secret
        self.access_token = self.get_access_token()

    def get_access_token(self) -> dict:
        """
        获取 access_token

        :return:
        """
        return requests.post(
            'https://api.dingtalk.com/v1.0/oauth2/accessToken',
            json={
                'appKey': self.app_key,
                'appSecret': self.app_secret,
            },
        ).json()['accessToken']

    def send(self, user_ids: List, content: str) -> dict:
        """
        发送消息

        :param user_ids: 用户 ID 列表
        :param content: 消息内容
        :return:
        """
        return requests.post(
            'https://api.dingtalk.com/v1.0/robot/oToMessages/batchSend',
            headers={
                'x-acs-dingtalk-access-token': self.access_token,
            },
            json={
                'robotCode': self.app_key,
                'userIds': user_ids,
                'msgKey': 'sampleText',
                'msgParam': str({
                    'content': content,
                })
            }
        ).json()