class DeepseekService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.deepseek.com/v1"

    def make_request(self, endpoint, params=None):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(f"{self.base_url}/{endpoint}", headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def search(self, query):
        endpoint = "search"
        params = {"query": query}
        return self.make_request(endpoint, params)

    def get_results(self, search_id):
        endpoint = f"results/{search_id}"
        return self.make_request(endpoint)