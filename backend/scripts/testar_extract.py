from app.services.pdf_service import ler_pdf
from app.services.extract_service import extrair_dados

CAMINHO = "uploads/teste.pdf"

texto = ler_pdf(CAMINHO)

dados = extrair_dados(texto)

print("=" * 60)
print("DADOS EXTRAÍDOS")
print("=" * 60)

print(dados)