# ☁️ Desafio de Projeto - Dio Step Functions

![Status](https://img.shields.io/badge/status-em%20andamento-yellow)
![AWS](https://img.shields.io/badge/AWS-Step%20Functions-orange?logo=amazon-aws)
![Lambda](https://img.shields.io/badge/AWS-Lambda-blue?logo=awslambda)
![S3](https://img.shields.io/badge/AWS-S3-green?logo=amazons3)

---

## 📌 Descrição

Este projeto tem como objetivo **consolidar workflows automatizados utilizando AWS Step Functions**, aplicando os conceitos aprendidos nas aulas da DIO.

O projeto envolve:

* Criação de **state machines** para automatizar processos na AWS
* Integração com funções **Lambda**
* Armazenamento e registro de logs no **S3**
* Simulação local completa para estudo e demonstração (mock de AWS)
* Documentação clara e estruturada para estudo e futuras implementações

---

## 🛠️ Tecnologias Utilizadas

* **AWS Step Functions** → Orquestração de workflows
* **AWS Lambda** → Execução de funções serverless
* **AWS S3** → Armazenamento de logs e outputs
* **Git & GitHub** → Versionamento e compartilhamento do projeto
* **Markdown** → Estruturação da documentação
* **Draw\.io / Lucidchart** → Criação de diagramas de arquitetura

---

## 📊 Arquitetura do Projeto

Exemplo de fluxo no **Step Functions**:

```
┌─────────────┐
│ Start       │
└─────┬───────┘
      ↓
┌─────────────┐
│ Lambda1     │ → Processamento de dados
└─────┬───────┘
      ↓
┌─────────────┐
│ Lambda2     │ → Envio de resultados para S3 / mock local
└─────┬───────┘
      ↓
┌─────────────┐
│ End         │
└─────────────┘
```

📌 Diagrama ilustrativo:
![Exemplo de Diagrama Step Functions](./images/exemplo-diagrama.png)

---

## 📂 Estrutura de Pastas e Arquivos

```
desafio-dio-step-functions/
│
├── README.md
├── .gitignore
├── /images
│   ├── exemplo-diagrama.png
├── /lambdas
│   ├── lambda1.py
│   ├── lambda2.py
│   └── test_workflow.py
├── /step-functions
│   └── workflow.json
└── /mock_aws
    ├── outputs/
    │   └── resultado.json
    ├── logs/
    │   └── exemplo-log.txt
    └── s3/
        └── exemplo-arquivo.txt
```

---

## 💡 Insights Pessoais

* **Step Functions** simplificam a automação sem servidores dedicados.
* **Lambda** é ideal para tarefas pequenas e modulares dentro do workflow.
* **Mock local** permite demonstrar o projeto sem conta AWS.
* Gravar outputs no **S3** ajuda na auditoria e depuração.
* Testar cada estado individualmente evita erros em produção.

---

## 📸 Evidências

* **Diagramas de arquitetura** → `![Step Function Execução](./images/step-function-print1.png)`
* **Mock AWS** → `/mock_aws` contém outputs, logs e arquivos S3 simulados

---

## 🔗 Recursos Úteis

* [AWS Step Functions - Documentação Oficial](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
* [AWS Lambda - Documentação Oficial](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
* [AWS S3 - Documentação Oficial](https://docs.aws.amazon.com/s3/index.html)
* [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)

---
