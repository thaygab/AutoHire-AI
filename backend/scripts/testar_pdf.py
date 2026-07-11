from app.services.pdf_service import ler_pdf

# Caminho do PDF para teste
CAMINHO_PDF = "uploads/teste.pdf"

texto = ler_pdf(CAMINHO_PDF)

print("=" * 60)
print("TEXTO EXTRAÍDO DO PDF")
print("=" * 60)

print(texto)