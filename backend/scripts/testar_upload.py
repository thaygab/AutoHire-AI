import requests

URL = "http://127.0.0.1:8000/upload"
ARQUIVO = "uploads/teste.pdf"

with open(ARQUIVO, "rb") as pdf:
    resposta = requests.post(
        URL,
        files={
            "arquivo": ("teste.pdf", pdf, "application/pdf")
        }
    )

print("=" * 60)
print("RESULTADO DO UPLOAD")
print("=" * 60)

print(f"Status Code: {resposta.status_code}")

try:
    print(resposta.json())
except Exception:
    print(resposta.text)