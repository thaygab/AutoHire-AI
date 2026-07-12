from app.services.knowledge_service import carregar_tecnologias

tecnologias = carregar_tecnologias()

print("=" * 60)
print("TECNOLOGIAS CARREGADAS")
print("=" * 60)

for tecnologia in tecnologias:
    print(tecnologia)