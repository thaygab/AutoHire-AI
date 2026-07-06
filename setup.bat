@echo off
title AutoHire AI - Setup

echo =====================================
echo        AutoHire AI - Setup
echo =====================================
echo.


:: =====================================================
:: AutoHire AI - Setup
:: Versão: 1.2.0
:: Descrição: Cria a estrutura inicial do projeto.
:: =====================================================
:: =====================================================
:: PASTAS PRINCIPAIS
:: =====================================================

if not exist frontend (
    mkdir frontend
)

if not exist backend (
    mkdir backend
)

if not exist docs (
    mkdir docs
)

if not exist database (
    mkdir database
)

if not exist uploads (
    mkdir uploads
)

if not exist reports (
    mkdir reports
)

if not exist prompts (
    mkdir prompts
)

:: =====================================================
:: DOCUMENTAÇÃO
:: =====================================================

if not exist docs\diario (
    mkdir docs\diario
)

if not exist docs\documentacao (
    mkdir docs\documentacao
)

if not exist docs\imagens (
    mkdir docs\imagens
)

if not exist docs\diagramas (
    mkdir docs\diagramas
)

:: =====================================================
:: BACKEND
:: =====================================================

if not exist backend\app (
    mkdir backend\app
)

if not exist backend\app\api (
    mkdir backend\app\api
)

if not exist backend\app\core (
    mkdir backend\app\core
)

if not exist backend\app\database (
    mkdir backend\app\database
)

if not exist backend\app\models (
    mkdir backend\app\models
)

if not exist backend\app\schemas (
    mkdir backend\app\schemas
)

if not exist backend\app\services (
    mkdir backend\app\services
)

if not exist backend\app\utils (
    mkdir backend\app\utils
)

if not exist backend\tests (
    mkdir backend\tests
)

if not exist backend\app\api\routes (
    mkdir backend\app\api\routes
)

:: =====================================================
:: FRONTEND
:: =====================================================

if not exist frontend\src (
    mkdir frontend\src
)

if not exist frontend\src\assets (
    mkdir frontend\src\assets
)

if not exist frontend\src\components (
    mkdir frontend\src\components
)

if not exist frontend\src\pages (
    mkdir frontend\src\pages
)

if not exist frontend\src\services (
    mkdir frontend\src\services
)

if not exist frontend\src\hooks (
    mkdir frontend\src\hooks
)

if not exist frontend\src\layouts (
    mkdir frontend\src\layouts
)

if not exist frontend\src\types (
    mkdir frontend\src\types
)

if not exist frontend\src\utils (
    mkdir frontend\src\utils
)

:: =====================================================
:: ARQUIVOS PRINCIPAIS
:: =====================================================

if not exist README.md (
    type nul > README.md
)

if not exist LICENSE (
    type nul > LICENSE
)

if not exist .gitignore (
    type nul > .gitignore
)

:: =====================================================
:: ARQUIVOS DE DOCUMENTAÇÃO
:: =====================================================

if not exist docs\CHANGELOG.md (
    type nul > docs\CHANGELOG.md
)

if not exist docs\versao2.md (
    type nul > docs\versao2.md
)

if not exist docs\diario\DIARIO_DESENVOLVIMENTO.md (
    type nul > docs\diario\DIARIO_DESENVOLVIMENTO.md
)

if not exist docs\documentacao\01-estrutura-do-projeto.md (
    type nul > docs\documentacao\01-estrutura-do-projeto.md
)

if not exist docs\documentacao\02-pastas.md (
    type nul > docs\documentacao\02-pastas.md
)

if not exist docs\documentacao\03-arquivos.md (
    type nul > docs\documentacao\03-arquivos.md
)

if not exist docs\documentacao\04-setup-bat.md (
    type nul > docs\documentacao\04-setup-bat.md
)

if not exist docs\documentacao\05-padroes-do-projeto.md (
    type nul > docs\documentacao\05-padroes-do-projeto.md
)

if not exist docs\documentacao\glossario.md (
    type nul > docs\documentacao\glossario.md
)

:: =====================================================
:: ARQUIVOS DO BACKEND
:: =====================================================

if not exist backend\app\main.py (
    type nul > backend\app\main.py
)

if not exist backend\requirements.txt (
    type nul > backend\requirements.txt
)

if not exist backend\.env.example (
    type nul > backend\.env.example
)

if not exist backend\app\api\__init__.py (
    type nul > backend\app\api\__init__.py
)

if not exist backend\app\api\router.py (
    type nul > backend\app\api\router.py
)

if not exist backend\app\api\routes\__init__.py (
    type nul > backend\app\api\routes\__init__.py
)

if not exist backend\app\api\routes\home.py (
    type nul > backend\app\api\routes\home.py
)

:: =====================================================
:: ARQUIVOS DO FRONTEND
:: =====================================================

if not exist frontend\src\App.tsx (
    type nul > frontend\src\App.tsx
)

echo.
echo =====================================
echo Projeto configurado com sucesso!
echo =====================================
echo.
pause