from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import date
import requests  

chrome_driver_path = ''

chrome_options = Options()
chrome_options.add_argument('--headless')  

# Impressora Lexmark MX611dhe
def get_counter_lexmark_MX611dhe(url, xpath):
    try:
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)  
        driver.get(url)
        counter_element = driver.find_element(By.XPATH, xpath)
        counter_text = counter_element.text.replace('= ', '')
        counter = int(counter_text)
        driver.quit()
        return counter
    except Exception:
        return "IP inacessível"
    
# Impressora Lexmark CX421adn
def get_counter_Lexmark_CX421adn(url, button_xpath, counter_xpath):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

        try:
            driver.get(url)
            time.sleep(3)
            
            # Clicar no botão para acessar o relatório
            botao = driver.find_element(By.XPATH, button_xpath)
            driver.execute_script("arguments[0].click();", botao)
            time.sleep(3)
            
            # Obter o contador da impressora SPIMA
            elemento = driver.find_element(By.XPATH, counter_xpath)
            
            if elemento:
                texto = elemento.text.strip()
            else:
                texto = "Elemento não encontrado."
        finally:
            driver.quit()
        return texto
    except Exception:
        return "IP inacessível"


# Impressora Samsung SL-M4070FR
def get_counter_samsung_SL_M4070FR(url, xpath):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

        try:
            driver.get(url)
            time.sleep(3)
            botao = driver.find_element(By.ID, "ext-gen249")
            botao.click()
            time.sleep(3)
            botao = driver.find_element(By.XPATH, '//*[@id="ext-gen150"]/div/li/ul/li[3]/div/a/span')
            driver.execute_script("arguments[0].click();", botao)
            time.sleep(3)
            elemento = driver.find_element(By.XPATH, xpath)
            if elemento:
                texto = elemento.text.strip()
            else:
                texto = "Elemento não encontrado."
        finally:
            driver.quit()
        return texto
    except Exception:
        return "IP inacessível"

# Impressora HP LaserJet Pro MFP M428fdw
def get_counter_hp_M428fdw(url, xpath):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

        try:
            driver.get(url)
            time.sleep(3)
            elemento = driver.find_element(By.XPATH, xpath)
            if elemento:
                texto = elemento.text.strip()
            else:
                texto = "Elemento não encontrado."
        finally:
            driver.quit()
        return texto
    except Exception:
        return "IP inacessível"
    
# Impressora HP LaserJet MFP M127 Fn
def get_counter_hp_M127(url, xpath):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

        try:
            driver.get(url)
            time.sleep(3)
            elemento = driver.find_element(By.XPATH, xpath)
            if elemento:
                texto = elemento.text.strip()
            else:
                texto = "Elemento não encontrado."
        finally:
            driver.quit()
        return texto
    except Exception:
        return "IP inacessível"
    
# Impressora HP LaserJet MFP M130fw
def get_counter_hp_M130(url, xpath):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

        try:
            driver.get(url)
            time.sleep(3)
            elemento = driver.find_element(By.XPATH, xpath)
            if elemento:
                texto = elemento.text.strip()
            else:
                texto = "Elemento não encontrado."
        finally:
            driver.quit()
        return texto
    except Exception:
        return "IP inacessível"
    
# Impressora HP LaserJet 400 M401dne
def get_counter_hp_M401dne(url, xpath):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

        try:
            driver.get(url)
            time.sleep(3)
            elemento = driver.find_element(By.XPATH, xpath)
            if elemento:
                texto = elemento.text.strip()
            else:
                texto = "Elemento não encontrado."
        finally:
            driver.quit()
        return texto
    except Exception:
        return "IP inacessível"

# Função para enviar o relatório para o Telegram
def send_report_to_telegram(report_message, bot_token, chat_id):
    """
    Envia a mensagem do relatório para o Telegram.
    """
    send_message_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": report_message,
        "parse_mode": "HTML"
    }
    response = requests.get(send_message_url, params=params)
    return response.json()


def generate_combined_report():
    today = date.today().strftime("%d-%m-%Y")  # Obter a data atual no formato desejado (dia-mês-ano)

    report_message = "𝗖𝗼𝗻𝘁𝗮𝗱𝗼𝗿 𝗱𝗲 𝗶𝗺𝗽𝗿𝗲𝘀𝘀𝗼𝗿𝗮𝘀: ({})\n".format(today)

    # Impressoras do contrato de Outsourcing de Impressão
    report_message += "Impressoras do contrato de Outsourcing de Impressão:\n"
    report_message += "🖨 Ajudância: {}\n".format(get_counter_lexmark_MX611dhe("http://10.34.117.80/cgi-bin/dynamic/printer/config/reports/deviceinfo.html", "/html/body/table[1]/tbody/tr[2]/td[2]/p"))
    report_message += "🖨 CIA: {}\n".format(get_counter_lexmark_MX611dhe("http://10.34.119.153/cgi-bin/dynamic/printer/config/reports/deviceinfo.html", "/html/body/table[1]/tbody/tr[2]/td[2]/p"))
    report_message += "🖨 SAIP: {}\n".format(get_counter_lexmark_MX611dhe("http://10.34.132.10/cgi-bin/dynamic/printer/config/reports/deviceinfo.html", "/html/body/table[1]/tbody/tr[2]/td[2]/p"))
    report_message += "🖨 Fiscalização: {}\n".format(get_counter_samsung_SL_M4070FR("http://10.34.118.69", "/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/fieldset[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div/div[3]/table/tbody/tr/td[6]/div"))

    # Adicionar espaço em branco
    report_message += "\n"

    # Impressoras própria do EB
    report_message += "Impressoras do EB:\n"
    report_message += "🖨 E1: {}\n".format(get_counter_samsung_SL_M4070FR("http://10.34.118.16", "/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/form/fieldset[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[1]/div[2]/div/div[3]/table/tbody/tr/td[6]/div"))
    report_message += "🖨 E4: {}\n".format(get_counter_hp_M428fdw("http://10.34.117.120/#hId-pgBizUsageReport", "/html/body/div[1]/div[5]/div[1]/div[2]/form/div[1]/div[1]/table/tbody/tr[2]/td[2]"))
    report_message += "🖨 AEMP: {}\n".format(get_counter_hp_M127("http://10.34.119.105/SSI/info_configuration.htm", "/html/body/div[2]/table/tbody/tr[2]/td[2]/div[5]/table/tbody/tr[1]/td[2]"))
    report_message += "🖨 Sec Infor: {}\n".format(get_counter_hp_M130("http://10.34.119.102/info_configuration.html?tab=Home&menu=DevConfig", "/html/body/div[2]/table/tbody/tr[2]/td[2]/div[7]/table/tbody/tr[1]/td[2]"))
    report_message += "🖨 Conformidade: {}\n".format(get_counter_hp_M401dne("http://10.34.119.10/info_configuration.html?tab=Home&menu=DevConfig", "/html/body/div[2]/table/tbody/tr[2]/td[2]/div[7]/table/tbody/tr[1]/td[2]"))
    report_message += "🖨 SPIMA: {}\n".format(get_counter_Lexmark_CX421adn("http://10.34.119.186/#/Settings/Reports/ReportDeviceGroup", "/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/ul/li[1]/div/a/span", "/html/body/div[1]/div[2]/div[4]/ul/li/div/ul/li/ul/li[1]/span[2]"))

    # Defina seu token de bot e ID de chat do canal
    bot_token = ''
    chat_id = ''

    # Envia o relatório para o Telegram
    send_report_to_telegram(report_message, bot_token, chat_id)

# Chamar a função para gerar e enviar o relatório combinado
generate_combined_report()
