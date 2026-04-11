from api.autentik_api import AutentikAPI

def test_reqres_auth_success():
    api = AutentikAPI()
    response = api.test_get_collections()
    
    # Biar muncul di terminal pas lo pake perintah -s
    print(f"\n[DEBUG] Status: {response.status_code}")
    print(f"[DEBUG] Response: {response.text}")
    
    assert response.status_code == 200