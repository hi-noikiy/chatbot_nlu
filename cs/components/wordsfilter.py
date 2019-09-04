from rasa.nlu.components import Component


class WordsFilter(Component):

    name = 'words_filter'
    provides = ["text"]
    language_list = ["zh"]

    def __init__(self, component_config=None):
        super(WordsFilter, self).__init__(component_config)
        self.words = self.component_config.get("filtered", [" "])
        print("Words filter components loaded successfully")

    def process(self, message, **kwargs):
        text = message.text
        for w in self.words:
            text = text.replace(w, '')
        message.text = text
