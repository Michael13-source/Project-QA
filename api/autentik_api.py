import requests

class AutentikAPI:
    def __init__(self):
        # Endpoint admin sesuai dashboard lo
        self.url = "https://reqres.in/api/collections" 
        self.headers = {
            "Content-Type": "application/json",
            # Server minta 'x-api-key' untuk admin calls
            "x-api-key": "pro_94cfe24ba776bdf557c9e4494466e77c2e9118526a4df93f"
        }

    def test_get_collections(self):
        # Langsung eksekusi tanpa Authorization: Bearer
        return requests.get(self.url, headers=self.headers)