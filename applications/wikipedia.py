#endpoint ricerca casuale: https://it.wikipedia.org/w/api.php?action=query&list=random&rnlimit=1&rnnamespace=0&format=json
#endpoint ricerca di qualcosa, aggiungenfo il titolo alla fine e sostituendo con replace ogni spazio con %20: https://it.wikipedia.org/w/api.php?prop=extracts&explaintext&exintro&format=json&action=query&titles=
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
import certifi
KV='''

'''

class WikiReader(MDApp):

    def build(self):
        self.title="WIKIPEDIA READER"
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Red"
        self.theme_cls.primary_hue="400"#aumentando aumento saturazione
        return Builder.load_file("wiki.kv")#posso mettere sia load string, ma con la stringa nel programma, sia nulla e la stringa in un altro programma, sia (se ci sono piu file kv), load file e mettere il nome del file

    def random_search_button(self):
        endpoint='https://it.wikipedia.org/w/api.php?action=query&list=random&rnlimit=1&rnnamespace=0&format=json'
        self.root.ids["mdlab"].text="caricamento in corso..."
        self.rs_request=UrlRequest(endpoint, on_success=self.get_data, ca_file=certifi.where())

    def get_data(self, *args, title=None):
        if title==None:
            response=args[1]
            title=response['query']['random'][0]['title']
        endpoint=f"https://it.wikipedia.org/w/api.php?prop=extracts&explaintext&exintro&format=json&action=query&titles={title.replace(' ', '%20')}"
        self.data_request=UrlRequest(endpoint, on_success=self.set_textarea, ca_file=certifi.where())
        
    def set_textarea(self, request, response):
        try:
            page_info=response['query']['pages']
            page_id=next(iter(page_info))
            titolo=page_info[page_id]['title']
            testo=page_info[page_id]['extract']
        except KeyError:
            testo="Errone, articolo non trovato"
        self.root.ids["mdlab"].text=f"{titolo}\n\n{testo}"

    def normal_search_button(self):
        query= self.root.ids["mdtext"].text
        self.get_data(title=query)

WikiReader().run()