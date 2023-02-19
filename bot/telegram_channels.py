import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
}
n = 'chats'


def get_data(url):
    with open(file=f"{n}.csv", mode='w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['линк', 'Ссылка', 'Название', 'Участники', 'Сообщение(7 дней)', 'MAU'])

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    d = soup.find('div', id='sticky-center-column').find_all('div', class_='card peer-item-row mb-2 ribbon-box border')

    for i in d:
        link = f"https://t.me/{i.find('a')['href'].split('@')[-1].split('/')[0]}"
        link_1_stolb = i.find('a')['href'].split('@')[-1].split('/')[0]
        title = i.find('div', class_='text-truncate font-16 text-dark mt-n1').text
        members = str(i.find('div', class_='text-truncate font-14 text-dark mt-n1').text.strip().split(' у')[0])
        messages_of_last_7_days = i.find_all('h4', class_='text-dark font-weight-normal mb-1 font-16 font-sm-18')[
            1].text.strip()
        mau = i.find_all('h4', class_='text-dark font-weight-normal mb-1 font-16 font-sm-18')[2].text.strip()

        if '.' in messages_of_last_7_days and 'k' in messages_of_last_7_days:
            messages_of_last_7_days = int(messages_of_last_7_days.replace('.', '').replace('k', '')) * 100
        elif '.' not in messages_of_last_7_days and 'k' in messages_of_last_7_days:
            messages_of_last_7_days = int(messages_of_last_7_days.replace('k', '')) * 1000

        if '.' in mau and 'k' in mau:
            mau = int(mau.replace('.', '').replace('k', '')) * 100
        elif '.' not in mau and 'k' in mau:
            mau = int(mau.replace('k', '')) * 1000

        with open(f"{n}.csv", 'a', encoding='utf-8-sig', newline='') as file_a:
            f = link_1_stolb, str(link), title, members, messages_of_last_7_days, mau
            writer = csv.writer(file_a, delimiter=';')
            writer.writerow(f)
