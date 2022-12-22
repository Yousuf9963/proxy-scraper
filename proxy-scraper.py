print("[+] Tool Namee:proxy-scraper")
print("[+] Author:Yousuf Shafi'i Muhammad.(Junior Programmer")
print("[+] Version:1.3")
print("[+] Team:Junior Programmers")
print("[+] Github:https://github.com/Yousuf9963/phone-num-info")
print("[+] Follow me on Github: https://github.com/Yousuf9963")
print("[-] Website muhammadabdirahman.wixsite.com/yousuf9963blog.")
print("[!] legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.")
print("[+] I hope for you good future and i am willing that you will come high effort.")
print("")
from bs4 import BeautifulSoup
import requests

filename = input("Enter the output filename : ")

url = 'https://free-proxy-list.net/'
r = requests.get(url)
content = r.content
soup = BeautifulSoup(content,'html.parser')

proxies = set()
table = soup.find('div',class_='table-responsive fpl-list')
body = table.find('tbody')
rows = body.find_all('tr')
for row in rows :
    ip = row.find('td')
    port = ip.findNext().text
    ip = ip.text
    print(f"{ip}:{port}")
    proxy = f"{ip}:{port}" 
    proxies.add(str(proxy+'\n'))
# for proxy in proxies:
with open(filename,'w')as f:
    f.writelines(proxies)
    # for proxy in proxies:
    