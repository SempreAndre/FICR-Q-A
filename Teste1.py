from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from time import sleep
#Service é um agente que usa o chrome driver para tomar controle do navegador em um versão especificada ou existente
servico = Service(ChromeDriverManager().install())
#inicia o serviço do navegador e atribui ele a variavel navegador
navegador = webdriver.Chrome(service=servico)
#diz para o navegador em que pagina abrir
navegador.get("file:///C:/Users/andre.franca/Downloads/1000/1000/index.html")
#teste1 campo nome em branco
campo = navegador.find_element(By.XPATH, '//*[@id="name"]')
campo.send_keys("")
usuario = navegador.find_element(By.XPATH, '//*[@id="username"]')
usuario.send_keys("Legend")
senha = navegador.find_element(By.XPATH, '//*[@id="password"]')  
senha.send_keys("123456789")
senha2 = navegador.find_element(By.XPATH, '//*[@id="password2"]')  
senha2.send_keys("123456789")
clickable = navegador.find_element(By.XPATH, '/html/body/main/form/button[1]')
ActionChains(navegador) \
    .click(clickable) \
    .perform()
sleep(5)
#teste2 campo username em branco
campo = navegador.find_element(By.XPATH, '//*[@id="name"]')
campo.send_keys("Andre")
usuario = navegador.find_element(By.XPATH, '//*[@id="username"]')
usuario.clear()
sleep(1)
usuario.send_keys("")
senha = navegador.find_element(By.XPATH, '//*[@id="password"]')  
senha.send_keys("123456789")
senha2 = navegador.find_element(By.XPATH, '//*[@id="password2"]')  
senha2.send_keys("123456789")
clickable = navegador.find_element(By.XPATH, '/html/body/main/form/button[1]')
ActionChains(navegador) \
    .click(clickable) \
    .perform()
sleep(5)
#teste3 campo password em branco
campo = navegador.find_element(By.XPATH, '//*[@id="name"]')
campo.send_keys("Andre")
usuario = navegador.find_element(By.XPATH, '//*[@id="username"]')
usuario.send_keys("Legend")
senha = navegador.find_element(By.XPATH, '//*[@id="password"]')  
senha.send_keys("")
senha2 = navegador.find_element(By.XPATH, '//*[@id="password2"]')  
senha2.send_keys("123456789")
clickable = navegador.find_element(By.XPATH, '/html/body/main/form/button[1]')
ActionChains(navegador) \
    .click(clickable) \
    .perform()
sleep(5)
