from api.autentik_api import AutentikAPI

def test_validasi_komentar():
    
    api = AutentikAPI()
    response = api.get_comments_by_post(1)
     
    assert response.status_code == 200
    assert len(response.json()) > 0