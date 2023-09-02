import httpx


def test_ping_endpoint():
    """
    Dado que el endpoint /v1/ping/ existe
    Cuando se hace una petición GET
    Entonces se obtiene una respuesta con status code 200 y el mensaje "pong!"
    """
    response = httpx.get("http://api:8000/v1/ping/")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
