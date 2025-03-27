# LinkedIn Job Scraper

Uma ferramenta simples para buscar vagas de emprego no LinkedIn com base em palavras chave, modalidade de trabalho e localização (ou opção remota). O script faz scraping de vagas no LinkedIn e salva os resultados em um arquivo `.csv`.

Um fork deste outro projeto: [https://github.com/Mean-Says/LinkedIn-Job-Scraper-CLI](https://github.com/Mean-Says/LinkedIn-Job-Scraper-CLI)

## Requisitos

- **Python 3.6+**
- **Poetry**
- **Bibliotecas necessárias**:
  - `requests`
  - `beautifulsoup4`
  - `python-decouple`

Para instalar as bibliotecas necessárias, execute:

```bash
pip install -r requirements.txt
```

## Como usar

### 1. Clone este repositório:

   ```bash
   git clone https://github.com/henriquesebastiao/linkedin-job-scraper
   ```

### 2. Acesse o diretório do projeto:

   ```bash
   cd linkedin-job-scraper
   ```

### 3. Variáveis de ambiente

Copie o conteúdo do arquivo `.env.example` para um arquivo `.env` na raiz do projeto e modifique as váriaveis. Este arquivo deve conter as seguintes variáveis:

- `SEARCH`: Palavras-chave para pesquisar no título da vaga. Exemplo: `"python,django,fastapi,desenvolvedor python"`.
- `LOCATION` (opcional): Localidade da vaga, valores possíveis:
   - `brasil` - valor default
   - `mt` - Mato Grosso
   - `go` - Goiás
- `REMOTE` (opcional): Modalidade de trabalho, Exemplo: `"remoto,hibrido"`. Valores possíveis:
   - `remoto`
   - `presencial`
   - `hibrido`

Agora carregue as variáveis de ambiente com o comando:

```shell
source .env
```

### 4. Execute o programa:

   ```bash
   python main.py
   ```

Após digitar o comando, a ferramenta irá buscar as vagas no LinkedIn e, se for bem-sucedida, salvará os resultados no arquivo `jobs.csv`.

## Via Docker

Voçê pode executar o script via docker, basta criar o arquivo .env como citado no passo anterior e executar o container com:

```shell
docker compose up -d
```

Da mesma forma, um arquivo `jobs.csv` deve ser gerado na sua pasta.

## Notas

- O scraper está sujeito a limitações do LinkedIn, como bloqueios temporários devido a um número excessivo de requisições (erro 429). Nesses casos, o programa automaticamente espera alguns segundos e tenta novamente.
- **Atenção**: O scraping de dados de sites pode violar os termos de uso do LinkedIn. Certifique-se de que o uso desta ferramenta esteja em conformidade com as políticas do site.
