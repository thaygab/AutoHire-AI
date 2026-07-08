# Glossário

Este documento reúne os principais termos utilizados durante o desenvolvimento do AutoHire AI.

---

# API (Application Programming Interface)

Permite que diferentes sistemas se comuniquem entre si.

No AutoHire AI, a API recebe solicitações do usuário e retorna uma resposta.

---

# Backend

Parte do sistema responsável pela lógica da aplicação.

É no backend que processamos arquivos, acessamos o banco de dados e utilizamos a inteligência artificial.

---

# Frontend

Parte visual da aplicação.

É a interface utilizada pelo usuário para interagir com o sistema.

---

# Router

Responsável por organizar as rotas da aplicação.

Cada rota recebe uma requisição e encaminha a execução para a camada responsável.

---

# Service

Camada responsável pela lógica de negócio.

É onde ficam as funcionalidades principais da aplicação.

Exemplo:

- salvar currículo;
- analisar currículo;
- gerar relatório.

---

# Upload

Processo de envio de um arquivo do computador do usuário para a aplicação.

---

# UploadFile

Classe do FastAPI utilizada para representar um arquivo enviado pelo usuário.

Ela permite acessar informações como:

- nome do arquivo;
- tipo do arquivo;
- conteúdo do arquivo.

---

# POST

Método HTTP utilizado para enviar informações para a aplicação.

Foi utilizado para realizar o upload de currículos.

---

# Path

Objeto da biblioteca `pathlib`.

Representa um caminho de arquivos ou pastas de forma segura e organizada.

---

# pathlib

Biblioteca do Python utilizada para manipular caminhos de arquivos e diretórios.

---

# shutil

Biblioteca do Python utilizada para copiar, mover e manipular arquivos.

---

# HTTPException

Classe do FastAPI utilizada para interromper a execução da aplicação e retornar um erro HTTP para o cliente.

Exemplo:

```python
raise HTTPException(
    status_code=400,
    detail="Apenas arquivos PDF são permitidos."
)
```

---

# Status Code

Código numérico retornado por uma API para indicar o resultado de uma requisição.

Exemplos:

- 200 → Requisição realizada com sucesso.
- 400 → Dados inválidos enviados pelo cliente.
- 404 → Recurso não encontrado.
- 500 → Erro interno do servidor.

---

# Bad Request (400)

Código HTTP utilizado quando o cliente envia uma requisição inválida.

No AutoHire AI é utilizado quando o usuário tenta enviar um arquivo diferente de PDF.