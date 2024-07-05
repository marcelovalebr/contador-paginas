# Contador de Impressoras com Relatório Diário

Este projeto é um script em Python que coleta contadores de diversas impressoras, gera um relatório e envia esse relatório para um canal do Telegram. Ele utiliza a biblioteca Selenium para automatizar a interação com as interfaces web das impressoras e a biblioteca Requests para enviar o relatório via API do Telegram.

## Funcionalidades

- Coleta contadores de várias impressoras de diferentes marcas e modelos.
- Gera um relatório com os contadores coletados.
- Envia o relatório gerado para um canal do Telegram.

## Impressoras Suportadas

- Lexmark MX611dhe
- Lexmark CX421adn
- Samsung SL-M4070FR
- HP LaserJet Pro MFP M428fdw
- HP LaserJet MFP M127 Fn
- HP LaserJet MFP M130fw
- HP LaserJet 400 M401dne

## Pré-requisitos

- Python 3.x
- Bibliotecas Python:
  - `selenium`
  - `requests`
- ChromeDriver (compatível com a versão do seu Google Chrome instalado)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Instale as dependências:
    ```bash
    pip install selenium requests
    ```

3. Baixe o ChromeDriver a partir de [aqui](https://sites.google.com/a/chromium.org/chromedriver/downloads) e coloque o caminho do ChromeDriver na variável `chrome_driver_path` no script.

## Configuração

1. Defina o caminho do ChromeDriver no script:
    ```python
    chrome_driver_path = '/caminho/para/seu/chromedriver'
    ```

2. Configure seu token de bot do Telegram e o ID do chat:
    ```python
    bot_token = 'seu_token_do_bot'
    chat_id = 'seu_id_do_chat'
    ```

## Uso

1. Execute o script:
    ```bash
    python seu_script.py
    ```

2. O script coletará os contadores das impressoras configuradas, gerará um relatório e enviará o relatório para o canal do Telegram configurado.

## Estrutura do Código

- Funções para obter contadores de diferentes modelos de impressoras.
- Função para gerar um relatório combinado com os contadores coletados.
- Função para enviar o relatório para um canal do Telegram.
