import requests

class AutentikAPI:
    def __init__(self):
        
        self.base_url = "https://jsonplaceholder.typicode.com"

    
    def get_comments_by_post(self, post_id):
        url = f"{self.base_url}/posts/{post_id}/comments"
        return requests.get(url)