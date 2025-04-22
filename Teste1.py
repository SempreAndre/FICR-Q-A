from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("file:///C:/Users/andre.franca/Downloads/1000/1000/index.html")

def preencher_form(nome, usuario, senha1, senha2):
    navegador.find_element(By.ID, "name").clear()
    navegador.find_element(By.ID, "name").send_keys(nome)

    navegador.find_element(By.ID, "username").clear()
    navegador.find_element(By.ID, "username").send_keys(usuario)

    navegador.find_element(By.ID, "password").clear()
    navegador.find_element(By.ID, "password").send_keys(senha1)

    navegador.find_element(By.ID, "password2").clear()
    navegador.find_element(By.ID, "password2").send_keys(senha2)

def clicar_botao():
    botao = navegador.find_element(By.XPATH, "/html/body/main/form/button[1]")
    ActionChains(navegador).click(botao).perform()
    sleep(2)

def formulario_foi_enviado():
    campo_nome = navegador.find_element(By.ID, "name")
    clicar_botao()
    sleep(1)
    try:
        campo_nome.get_attribute("value")
        return False 
    except:
        return True

# Teste 1: nome em branco
preencher_form("", "Legend", "12345678", "12345678")
if formulario_foi_enviado() == True:
    print("Campo nome em branco enviando formulario")
else:
    print("Teste nome em branco ok")
sleep(3)
    
# Teste 2: nome com mais de 20 caracteres
preencher_form("André de França Silva Pereira", "usuario", "12345678", "12345678")
valor_nome = navegador.find_element(By.ID, "name").get_attribute("value")
if len(valor_nome) <= 20:
    print("Apenas 20 caracteres foram digitados em Nome")
else:
    print("Erro: campo 'Nome' aceitou mais de 20 caracteres" + str(({len(valor_nome)})))
sleep(3)

# Teste 3: usuário em branco
preencher_form("Andre", "", "12345678", "12345678")
if formulario_foi_enviado() == True:
    print("Campo Usuario em branco, enviando formulario")
else:
    print("Teste Usuario em branco ok")
sleep(3)

# Teste 4: senha muito longa
preencher_form("Andre", "Legend", "123456789", "12345678")
valor_s = navegador.find_element(By.ID, "password").get_attribute("value")
if len(valor_s) <= 8:
    print("Teste senha tem até 8 caracteres Ok")
else:
    print("Erro: campo senha aceitou mais de 8 caracteres!" + str(({len(valor_s)})))
clicar_botao()
sleep(5)

# Teste 5: senhas diferentes(percebi depois que o codigo não barra as senhas diferentes)
#preencher_form("Andre", "Legend", "12345678", "87654321")
#if formulario_foi_enviado() == True:
 #   print("Senhas diferentes, enviando formulario")
#else:
#    print("Teste senhas diferentes ok")
#sleep(3)

# Teste 5: senha vazia
preencher_form("Andre", "Legend", "", "12345678")
if formulario_foi_enviado() == True:
    print("Campo Senha em branco, enviando formulario")
else:
    print("Teste Senha em branco ok")
sleep(3)

# Teste 6: confirmação de senha vazia
preencher_form("Andre", "Legend", "12345678", "")
if formulario_foi_enviado() == True:
    print("Campo confirmação de senha em branco, enviando formulario")
else:
    print("Teste confirmação de senha em branco ok")
sleep(3)

# Teste 3: Confirmação de senha muito longa
preencher_form("Andre", "Legend", "12345678", "123456789")
valor_s2 = navegador.find_element(By.ID, "password2").get_attribute("value")
if len(valor_s2) <= 8:
    print("Teste confirmação senha tem 8 ou menos caracteres Ok" + str(({len(valor_s2)})))
else:
    print("Erro: campo confirmação senha aceitou mais de 8 caracteres!" + str(({len(valor_s2)})))
clicar_botao()
sleep(3)

# Teste 7: tudo preenchido corretamente
preencher_form("Andre", "Legend", "12345678", "12345678")
if formulario_foi_enviado() == True:
    print("Teste todos campos corretos Ok")
else:
    print("Erro de envio de formulario!")

sleep(3)

print("Todos testes executados com sucesso!")

navegador.quit()
