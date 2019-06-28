from weibopy import WeiboOauth2, WeiboClient
from collections import defaultdict
import webbrowser
import time

client_key = '3108629810'
client_secret = '7a3024d73e832f4309b57e35fb35748f'
redirect_url = 'https://api.weibo.com/oauth2/default.html'

auth = WeiboOauth2(client_key,client_secret,redirect_url)

webbrowser.open_new(auth.authorize_url)

code = input('输入：')

token = auth.auth_access(code)

print(token)

client = WeiboClient(token['access_token'])

'''result = client.get(suffix='comments/show.json',params={'id':4322140368509204,'count':200,'page':1})'''

province_list = defaultdict(list)
comment_text_list = []
for i in range (1,5):
    result = client.get(suffix='comment/show.json',params={'id':4322140368509204,'count':200,'page':i})
    comments = result['comments']
    if not len(comments):
        break

    for comment in comments:
        text = re.sub('回复.*?：', '', str(comment['text']))
        province_list[province].append(text)
        comment_text_list.append(text)
    print('已抓取评论{}条'.format(len(comment_text_list)))
    time.sleep(1)
