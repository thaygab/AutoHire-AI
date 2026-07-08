# Solução de Problemas

Este documento reúne os principais problemas encontrados durante o desenvolvimento do AutoHire AI e suas respectivas soluções.

---

# Problema

## Erro ao fazer upload de arquivos

### Mensagem

```text
Form data requires "python-multipart" to be installed.
```

### Causa

O FastAPI necessita da biblioteca `python-multipart` para trabalhar com envio de arquivos (`multipart/form-data`).

### Solução

Instalar a biblioteca:

```bash
pip install python-multipart
```

Depois atualizar as dependências do projeto:

```bash
pip freeze > requirements.txt
```

---

# Problema

## PowerShell bloqueando o ambiente virtual

### Mensagem

```text
Execution of scripts is disabled on this system.
```

### Causa

Por padrão, o PowerShell impede a execução de scripts por questões de segurança.

### Solução

Executar:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois ativar novamente o ambiente virtual:

```powershell
.\venv\Scripts\Activate.ps1
```

---

# Problema

## Servidor da API não responde

### Possíveis causas

- O servidor (`uvicorn`) foi encerrado.
- O computador entrou em suspensão.
- O terminal do servidor foi fechado.

### Solução

Executar novamente:

```powershell
uvicorn app.main:app --reload
```

Verificar se aparece a mensagem:

```text
Application startup complete.
```