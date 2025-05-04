import os
from dotenv import load_dotenv

# Configurações iniciais
load_dotenv()  # Carrega variáveis do arquivo .env

def calcular_rota(origem: str, destino: str) -> dict:
    """Calcula rota usando OpenRouteService (versão gratuita)."""
    print(f"🛣️  Calculando rota: {origem} → {destino}")
    # (Aqui você integrará a API depois)
    return {"distancia_km": 42.0, "tempo_min": 60}

if __name__ == "__main__":
    # Exemplo de uso
    rota = calcular_rota("São Paulo", "Rio de Janeiro")
    print(f"📊 Resultado: {rota}")
