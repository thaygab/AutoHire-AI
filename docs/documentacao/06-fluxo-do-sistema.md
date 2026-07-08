# Fluxo do Sistema

## Objetivo

Este documento descreve o funcionamento das funcionalidades do AutoHire AI.

Seu objetivo é explicar como as informações percorrem o sistema, desde a entrada do usuário até o resultado final.

---

# Upload de Currículo

## Objetivo

Receber um currículo enviado pelo usuário e armazená-lo na pasta de uploads.

---

## Fluxo

Usuário

↓

Seleciona um currículo em PDF

↓

Envia o arquivo para a API

↓

Rota `/upload`

↓

Serviço `salvar_curriculo()`

↓

Pasta `uploads`

↓

Currículo salvo

---

## Explicação

### Usuário

Seleciona um currículo em seu computador através da interface da aplicação.

---

### Rota `/upload`

Recebe o arquivo enviado.

Sua responsabilidade é apenas receber a requisição e encaminhar o arquivo para o serviço responsável.

Ela não possui regras de negócio.

---

### Serviço `salvar_curriculo()`

Responsável por:

- criar a pasta de uploads caso ela não exista;
- definir o caminho onde o arquivo será salvo;
- copiar o conteúdo do currículo;
- retornar o resultado da operação.

---

### Pasta `uploads`

Armazena os currículos enviados para o sistema.

---

## Resultado

Ao final do processo, o currículo encontra-se salvo na pasta `uploads`.