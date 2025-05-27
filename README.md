
# 🖨️ Automação de Coleta de Contadores de Impressoras

Script em **Python** que utiliza **Selenium** para automatizar a **coleta diária de contadores de impressoras** e enviar **relatórios via Telegram**.

Desenvolvido para ambientes de **Infraestrutura Crítica**, com foco em **eficiência operacional**, **redução de falhas humanas** e **monitoramento automatizado** de diversos modelos de impressoras.

---

## 🚀 Funcionalidades

✅ Coleta automatizada de contadores de diversas impressoras (Lexmark, HP, Samsung).  
✅ Utiliza **Selenium** para navegação web e extração de dados.  
✅ Geração de **relatório consolidado** com informações coletadas.  
✅ Envio automático do relatório via **Telegram Bot**.  
✅ Execução em modo **headless** (sem interface gráfica).

---

## 🛠️ Tecnologias utilizadas

- **Python 3.x**  
- **Selenium**  
- **requests** (integração com API do Telegram)  
- **Chrome WebDriver**

---

## ⚙️ Como usar

1. Clone este repositório:  
```bash
git clone https://github.com/marcelovalebr/contador-paginas.git
cd contador-paginas
```

2. Instale as dependências:  
```bash
pip install selenium requests
```

3. Configure o **`chrome_driver_path`** no script para apontar para o local do **ChromeDriver** na sua máquina.

4. Configure o **bot token** e o **chat ID** do **Telegram** no final do script:  
```python
bot_token = 'SEU_TOKEN'
chat_id = 'SEU_CHAT_ID'
```

5. Execute o script:  
```bash
python contador_paginas.py
```

---

## 📊 Impressoras suportadas

- Lexmark MX611dhe  
- Lexmark CX421adn  
- Samsung SL-M4070FR  
- HP LaserJet Pro MFP M428fdw  
- HP LaserJet MFP M127 Fn  
- HP LaserJet MFP M130fw  
- HP LaserJet 400 M401dne

---

## 🛡️ Aplicações práticas

✅ Monitoramento automatizado de **parques de impressoras**.  
✅ **Relatórios periódicos** enviados via Telegram para equipes de suporte.  
✅ Redução de **trabalho manual** e **minimização de falhas**.  
✅ Uso em ambientes com necessidade de **disponibilidade e controle rigoroso**.

---

## 👨‍💻 Autor

**Marcelo Vale**  
Especialista em Segurança da Informação | Automação de Processos | Infraestrutura Crítica  

[GitHub](https://github.com/marcelovalebr) | [LinkedIn](https://www.linkedin.com/in/marcelovalebr/)

---

## 📝 Licença

Este projeto está licenciado sob a **MIT License** — veja o arquivo **LICENSE** para mais detalhes.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para **forkar** e sugerir melhorias.
