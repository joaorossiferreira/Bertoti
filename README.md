# 🚀 Tradutor de Regras de Negócio para Código Python

## 🤖 Trabalho IA Agente IHC - Conversor Inteligente de Requisitos

**Objetivo:** Desenvolver um agente inteligente capaz de interpretar regras de negócio em linguagem natural e convertê-las automaticamente em código Python funcional.

### ✨ Exemplo Prático:

**Entrada (Regra de Negócio):**  
*"Se o valor da compra for superior a R$ 200, aplicar desconto de 10%"*

**Saída (Código Python):**
```python
def aplicar_desconto(valor_compra):
    if valor_compra > 200:
        return valor_compra * 0.9
    return valor_compra
```

### 🔍 Escopo do Projeto:
Foco inicial em domínios específicos para validação do conceito:
- Cálculo de descontos e promoções
- Políticas de frete e envio
- Cálculo de impostos básicos

---

## 👥 Equipe

| Integrante       | LinkedIn | GitHub |
|------------------|----------|--------|
| **Eduardo Fontes** | [🔗 Perfil](https://www.linkedin.com/in/eduardo-da-silva-fontes/) | [💻 DuuhZero](https://github.com/DuuhZero) |
| **João França**    | [🔗 Perfil](https://www.linkedin.com/in/joão-pedro-frança-alves-de-souza-8700a62b3/) | [💻 jofran2001](https://github.com/jofran2001) |
| **João Rossi**     | [🔗 Perfil](https://www.linkedin.com/in/eduardo-da-silva-fontes/) | [💻 DuuhZero](https://github.com/DuuhZero) |
| **Paulo Almeida**  | [🔗 Perfil](https://www.linkedin.com/in/paulo-almeida-3102452a7/) | [💻 pauloalmeida46](https://github.com/pauloalmeida46) |

---

## 🛠 Tecnologias Previstas
- Processamento de Linguagem Natural (NLP)
- Framework Rasa ou similar
- Python 3.x
- Git para controle de versão

*"Transformando requisitos em implementações de forma inteligente"* 🤖💡

## ▶️ Como rodar?
- Verifique se o Ollama está rodando:
 ```shell
 ollama serve
 ``` 
 - Dê pull na última versão do Mistral (agente usado neste caso):
 ```shell
 ollama run mistral:latest
 ``` 
 - Verifique os modelos:
 ```shell
 ollama list
 ```
 - Navegue até o diretório e instale as dependências:
 ```shell
 cd negocios-python-main

 cd requisitos-para-codigo

 pip install -r requirements.txt
```
- Rode o projeto
```shell
python main.py
``` 
 - Caso o projeto esteja muito pesado, digite o comando para apagar:
 ```shell
 ollama rm <nome_do_modelo>
 ``` 
