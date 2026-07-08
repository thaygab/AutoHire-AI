# 📘 Diário de Desenvolvimento — AutoHire AI

## Sobre este documento

Este diário registra toda a evolução do projeto **AutoHire AI**, desde sua criação até a versão final.

O objetivo é documentar cada etapa do desenvolvimento, registrar decisões técnicas, explicar o que foi aprendido e facilitar futuras manutenções e melhorias.

---

# Etapa 1 — Estrutura inicial do projeto

**Data:** 05/07/2026

## Objetivo

Preparar o ambiente do projeto para iniciar o desenvolvimento de forma organizada e profissional.

## Atividades realizadas

* Criação da estrutura inicial de pastas.
* Criação dos arquivos principais do projeto.
* Criação do script `setup.bat` para automatizar a estrutura.
* Inicialização do Git.
* Alteração da branch principal para `main`.

## Conceitos aprendidos

* O Git registra o histórico completo do projeto.
* A pasta `.git` contém todas as informações de versionamento.
* Arquivos marcados como **Untracked** ainda não estão sendo monitorados pelo Git.
* A branch `main` é utilizada como branch principal do projeto.

## Decisões da Versão 1

### Arquitetura

* Frontend: React + TypeScript + Vite
* Backend: FastAPI
* Banco de dados: PostgreSQL
* ORM: SQLAlchemy
* Validação: Pydantic

### Organização

Foi definida uma estrutura de pastas fixa para manter o projeto organizado.

Alterações na arquitetura somente serão realizadas caso exista um erro grave.

Melhorias futuras serão registradas para a **Versão 2**.

## Dificuldades encontradas

Nenhuma.

## Resultado

Estrutura inicial criada com sucesso e projeto preparado para o início do desenvolvimento.

---

## Próxima etapa

Configurar os arquivos iniciais do projeto (`README.md`, `.gitignore` e `LICENSE`) antes de iniciar o desenvolvimento do backend.

# Etapa 1.1 — Evolução do setup.bat

## Objetivo

Tornar o script de criação do projeto seguro para ser executado mais de uma vez.

## Atividades realizadas

* Adicionada verificação antes da criação de pastas.
* Adicionada verificação antes da criação de arquivos.
* O script não sobrescreve mais arquivos existentes.
* O script não tenta recriar pastas já existentes.

## Resultado

O `setup.bat` passou a ser reutilizável, permitindo sua execução diversas vezes sem risco de perda de conteúdo.

## Próxima melhoria

Automatizar a criação do ambiente virtual Python.

# Diário de Desenvolvimento

---

# Data 07/07

---

# Funcionalidade

## Upload de Currículo

---

## Objetivo

Implementar a primeira funcionalidade completa do AutoHire AI.

O objetivo desta etapa foi permitir que a aplicação recebesse um currículo enviado pelo usuário e o armazenasse na pasta `uploads`.

---

## O que foi desenvolvido

- Estrutura da rota de upload.
- Criação do serviço de upload.
- Recebimento de arquivos utilizando FastAPI.
- Salvamento do currículo na pasta `uploads`.
- Organização da arquitetura em camadas (Router → Service).

---

## Problemas encontrados

### Biblioteca `python-multipart`

O FastAPI apresentou erro ao receber arquivos.

**Solução**

Instalação da biblioteca:

```bash
pip install python-multipart