# FICR-Q-A
Repositorio para codigos da cadeira de testes automatizados da faculdade

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente de `<Python/ Selenium / webdriver-manager>`
- Você tem uma máquina `<Windows / Linux / Mac>`. 

# Teste.py
Atividade realizada para automatizar teste em campos de formulario com o objetivo de conferir se as restrições em codigo estão funcionando corretamente.

Teste consiste em:

  1. Criar função para preencher o formulario com diversas alternativas;
  2. Criar função para clicar no botão de cadastrar;
  3. criar função para verificar se o formulário foi enviado com sucesso;
  4. Testar se o campo nome em branco(sem preenchimento) é enviado, acusar quando for enviado ou quando não for enviado;
  5. Testar se o campo nome preenchido com mais caracteres que o permitido é enviado, acusar a quantidade de caracteres digitados se passou ou não;
  6. Testar se o campo usuário em branco(sem preenchimento) é enviado;
  7. Testar se o campo senha tem a quantidae de caracteres permitidos, acusando a quantidade de caracteres e se é enviado com sucesso ou não;
  8. Testar se o campo senha em branco(sem preenchimento) é enviado;
  9. Testar se o campo confirmar senha tem a quantidae de caracteres permitidos, acusando a quantidade de caracteres e se é enviado com sucesso ou não;
  8. Testar se o campo confirmar senha em branco(sem preenchimento) é enviado;
  9. Testar se o formulario preenchido corretamente é enviado.

# Teste-unitario-carga
Atividade proposta em sala para realização de testes em um unico campo avaliando no minimo 3 restrições do mesmo.

Teste consiste em:

  1. Criar função para preencher o campo usuário com diversas alternativas;
  2. Criar função para clicar no botão de cadastrar;
  3. criar função para verificar se o formulário foi enviado com sucesso;
  4. criar loop para teste de carga com um numero máximo de repetições;
  5. Testar se o campo usuário em branco(sem preenchimento) é enviado, acusar quando for enviado ou quando não for enviado;
  6. Testar se o campo usuário preenchido com mais caracteres que o permitido é enviado, acusar a quantidade de caracteres digitados se passou ou não;
  7. Testar se o campo usuário preenchido com menos caracteres que o permitido é enviado, acusar a quantidade de caracteres digitados se passou ou não;
  8. Testar se o campo usuário preenchido com caracteres não permitidos é enviado com sucesso ou não;
  9. Testar se o campo usuário preenchido corretamente é enviado;
