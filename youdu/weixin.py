from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk.basic import WechatBasic

from youdu.menu import MENU, WELCOME_MSG

TOKEN = 'TesTWeixiN'

@csrf_exempt
def weixinapi(request):
    wechat = WechatBasic(token=TOKEN)
    if 'echostr' in request.GET:
        result = wechat.check_signature(signature=request.GET['signature'],
                                        timestamp=request.GET['timestamp'],
                                        nonce=request.GET['nonce'])
        if result:
            return HttpResponse(request.GET['echostr'])
        else:
            return HttpResponse()

    message = request.body
    response = process_msg(wechat, message)
    return HttpResponse(response)

def process_msg(wechat, data):
    wechat.parse_data(data)
    msg = wechat.get_message()

    response = None
    if msg.type == 'text' and msg.content == u'新闻':
        response = wechat.response_news([
            {
                'title': u'京东网',
                'picurl': u'http://doraemonext.oss-cn-hangzhou.aliyuncs.com/test/wechat-test.jpg',
                'url': u'http://www.jd.com/',
            }, {
                'title': u'V2EX',
                'picurl': u'http://doraemonext.oss-cn-hangzhou.aliyuncs.com/test/wechat-test.jpg',
                'url': u'http://www.v2ex.com/',
            }, {
                'title': u'taobao',
                'picurl': u'http://doraemonext.oss-cn-hangzhou.aliyuncs.com/test/wechat-test.jpg',
                'url': u'http://www.taobao.com/',
            }
        ])
    elif msg.type == 'subscribe':
        response = wechat.response_text(WELCOME_MSG)
    else:
        response = wechat.response_text(u'');
    return response

def weixin_init(request):
    wechat = WechatBasic(appid=settings.WECHAT_APPID, appsecret=settings.WECHAT_APPSECRET)
    ret = wechat.create_menu(MENU)
    return HttpResponse(ret)
