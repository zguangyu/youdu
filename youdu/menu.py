# -*- coding: utf-8 -*-
import urllib.parse
from django.conf import settings

url_redirect = 'https://open.weixin.qq.com/connect/oauth2/authorize?response_type=code&scope=%(scope)s&state=123&appid=%(appid)s&redirect_uri=%(uri)s#wechat_redirect'

MENU = {
    'button':[
        {
            'type': 'view',
            'name': u'游你定',
            'url': url_redirect % {'appid':settings.WECHAT_APPID, 'uri':urllib.parse.quote_plus('http://weixin.guangyu.me/'), 'scope':'snsapi_base'}
        },
        {
            'type': 'view',
            'name': u'聚宝盆',
            'url': url_redirect % {'appid':settings.WECHAT_APPID, 'uri':urllib.parse.quote_plus('http://weixin.guangyu.me/'), 'scope':'snsapi_base'}
        },
    ]
}

WELCOME_MSG = "Hello"
