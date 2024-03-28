import requests
import json
import threading

def write_file(f_path, text):
    with open(f_path, "at", encoding='utf-8') as f:
        f.write(text + "\n")

def check_proxy(proxy, proxy_type):
    try:



        proxies = {
            'http': f'{proxy_type}://{proxy}',
            'https': f'{proxy_type}://{proxy}'
        }
        r = requests.get("http://ipwho.is/", proxies=proxies)
        data = r.text



        parsed_data = json.loads(data)

        country = parsed_data['country']
        region = parsed_data['region']


        print(f"Страна прокси: {country} регион:{region}, proxy: {proxy} ")
        write_file('goodProxy.txt', proxy)

        if country == 'France':
            print('Francie')
        if country == 'Russia':

            write_file('ruusia.txt', proxy)


    except Exception as e:
        with open('bad.txt', 'a') as f:
            f.write(proxy + '\n')

proxy_type = input("Выберите тип прокси (Socks5, HTTP, socks4): ")

with open('proxy.txt') as f:
    proxies = f.read().splitlines()

threads = []

for proxy in proxies:
    thread = threading.Thread(target=check_proxy, args=(proxy, proxy_type))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
