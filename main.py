import os
from openrouteservice import Client
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTE_API_KEY")

def calcular_rota(origem: list, destino: list) -> dict:
    """Calcula rotas usando OpenRoute.ai. Coordenadas = [longitude, latitude]."""
    try:
        client = Client(key=api_key)
        rota = client.directions(
            coordinates=[origem, destino],
            profile='driving-car',
            format='json'
        )
        distancia_km = rota['routes'][0]['summary']['distance'] / 1000
        tempo_min = rota['routes'][0]['summary']['duration'] / 60
        return {"distancia_km": round(distancia_km, 2), "tempo_min": round(tempo_min, 2)}
    except Exception as e:
        return {"erro": str(e)}

if __name__ == "__main__":
    # Exemplo: São Paulo -> Rio (coordenadas [long, lat])
    resultado = calcular_rota(
        origem=[-46.6333, -23.5505],  # Longitude, Latitude de SP
        destino=[-43.1729, -22.9068]   # Longitude, Latitude do RJ
    )
    print("🔍 Resultado:", resultado)
