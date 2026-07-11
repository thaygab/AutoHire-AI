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

## [09/07/2026]

### Adicionado
- Implementado o serviço `pdf_service.py` para leitura de arquivos PDF.
- Adicionada a biblioteca PyMuPDF para extração de texto.
- Criado script de teste para validar a leitura de PDFs.
- Criada estrutura inicial para testes do backend.

### Alterado
- Aprimorado o `setup.bat` com criação automática da estrutura de testes.
- Automatizada a criação dos arquivos `__init__.py`.
- Revisada a arquitetura do projeto.
- Atualizado o `.gitignore`.