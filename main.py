import requests
import time
from bs4 import BeautifulSoup
from decouple import config


geo_ids = {
    'brasil': 106057199,
    'mt': 103076538,
    'go': 104679607,
}

remote_options = {
    'remoto': 2,
    'presencial': 1,
    'hibrido': 3,
}

search = config('SEARCH', cast=str)
location = config('LOCATION', default='', cast=str)
remote = config('REMOTE', default='', cast=str)

def format_combination(entry: str, options: dict):
    data = entry.split(',')
    data_id = [str(options[option]) for option in data]
    return "%2C".join(data_id)

url = f'https://www.linkedin.com/jobs/search?keywords={search}&trk=public_jobs_jobs-search-bar_search-submit'

if location:
    url += f'&geoId={geo_ids[location]}'
else:
    url += f'&geoId={geo_ids[brasil]}'

if remote:
    remote = format_combination(remote, remote_options)
    url += f'&f_WT={remote}'


print(url)

class Job():
    def __init__(self, title, link):
        self.title = title
        self.link = link

    def to_json(self):
        return {
            'title': self.title,
            'link': self.link
        }

def save_to_file(jobs):
    with open("jobs.csv", 'w', encoding='utf-8') as file:
        for job in jobs:
            file.write(f"{job.title},{job.link}\n")

# Loop para tentar novamente em caso de erro de requisição.
while True:
    try:
        # Atraso para evitar o erro 429 (Too Many Requests).
        time.sleep(2)

        # Faz a requisição HTTP.
        html = requests.get(url)
        if html.status_code == 200:
            bs = BeautifulSoup(html.text, 'html.parser')

            # Busca pelos links e títulos das vagas.
            jobs_list = bs.find_all('a', {'class': 'base-card__full-link'})

            jobs = set()
            for job in jobs_list:
                title = job.get_text(strip=True)
                link = job['href']
                jobs.add(Job(title, link))

            save_to_file(jobs)
            break

        else:
            print(f"Erro na requisição: {html.status_code}")
            time.sleep(5)  # Espera 5 segundos antes de tentar novamente.
            print("Tentando novamente em 5 segundos...")

    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(5)  # Espera 5 segundos antes de tentar novamente.
        print("Tentando novamente em 5 segundos...")
