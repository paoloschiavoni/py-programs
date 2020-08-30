#endpoint ricerca casuale: https://it.wikipedia.org/w/api.php?action=query&list=random&rnlimit=1&rnnamespace=0&format=json
#endpoint ricerca di qualcosa, aggiungenfo il titolo alla fine e sostituendo con replace ogni spazio con %20: https://it.wikipedia.org/w/api.php?prop=extracts&explaintext&exintro&format=json&action=query&titles=
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest
import certifi

KV='''
Screen:

    GridLayout:
        rows:4

        MDLabel:
            id: mdlab
            text: "benvenuto su wikipedia reader"
            #font_style: "H3"
            padding_x: 30
            #size_hint_y: None
            #halign: "right"
            text_size: self.width, None#larghezza: larghezza in se, altezza illiminata, quindi posso avere lo scrolling

        MDRaisedButton:
            id: mdbu1
            text: "cerca articolo casuale"
            size_hint_x:1 #usato in percentuale
            on_press: app.random_search_button()

        MDTextFieldRect:

            id: mdtext
            hint_text: "cerca la parola che ti interessa"
            size_hint: 1, None
            height: "30dp"

        MDRaisedButton:
            id: mdbu2
            text: "cerca articolo interessato"
            size_hint_x:1 #usato in percentuale
            on_press: app.cerca_articolo()
'''

class WikiReader(MDApp):

    def build(self):
        self.title="WIKIPEDIA READER"
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Red"
        self.theme_cls.primary_hue="400"#aumentando aumento saturazione
        return Builder.load_string(KV)

    def random_search_button(self):
        endpoint='https://it.wikipedia.org/w/api.php?action=query&list=random&rnlimit=1&rnnamespace=0&format=json'
        self.root.ids["mdlab"].text="caricamento in corso..."
        self.rs_request=UrlRequest(endpoint, on_success=self.get_data, ca_file=certifi.where())

    def get_data(self, request, response):
        random_title=response['query']['random'][0]['title']
        endpoint=f"https://it.wikipedia.org/w/api.php?prop=extracts&explaintext&exintro&format=json&action=query&titles={random_title.replace(' ', '%20')}"
        self.data_request=UrlRequest(endpoint, on_success=self.set_textarea, ca_file=certifi.where())
        
    def set_textarea(self, request, response):
        page_info=response['query']['pages']
        page_id=next(iter(page_info))
        titolo=page_info[page_id]['title']
        testo=page_info[page_id]['extract']
        self.root.ids["mdlab"].text=f"\n\n\n{titolo}\n\n{testo}"

    def cerca_articolo(self):
        titolo= self.root.ids["mdtext"].text
        if titolo=='':
            self.root.ids["mdlab"].text='Errore: nome dell\'articolo non fornito'
        else:
            self.root.ids["mdlab"].text="caricamento in corso..."
            endpoint=f"https://it.wikipedia.org/w/api.php?prop=extracts&explaintext&exintro&format=json&action=query&titles={titolo.replace(' ', '%20')}"
            self.data_request=UrlRequest(endpoint, on_success=self.set_textarea, ca_file=certifi.where())

WikiReader().run()