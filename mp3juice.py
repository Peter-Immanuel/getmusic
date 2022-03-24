from engine.root import BaseEngine


class Search(BaseEngine):
    engine_name = "mp3juice"
    api_path = "api.php"

    def __init__(self):
        super().__init__()
        self.site_uri = "https://mp3-juice.com/"
        self.request_method = self.GET
        self.response_type = self.JSON

    def get_url_path(self, page=None, category=None):
        return self.api_path

    def parse_object(object):
        """Parse JSON OBJECT To extract download_links,arts,and song_titles"""
        return
