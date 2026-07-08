# Comandos Úteis

Este documento reúne os comandos utilizados durante o desenvolvimento do AutoHire AI.

---

# Navegação

Entrar na pasta do backend

```powershell
cd backend
```

Voltar uma pasta

```powershell
cd ..
```

---

# Ambiente Virtual

Ativar o ambiente virtual (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

Criar ambiente virtual

```powershell
python -m venv venv
```

---

# Dependências

Instalar uma biblioteca

```powershell
pip install nome-da-biblioteca
```

Atualizar o requirements.txt

```powershell
pip freeze > requirements.txt
```

Instalar todas as dependências

```powershell
pip install -r requirements.txt
```

---

# Backend

Iniciar o servidor

```powershell
uvicorn app.main:app --reload
```

---

# Git

Verificar alterações

```powershell
git status
```

Adicionar arquivos

```powershell
git add .
```

Criar um commit

```powershell
git commit -m "mensagem"
```

Enviar alterações

```powershell
git push
```

---

# Testes

Abrir documentação da API

http://127.0.0.1:8000/docs