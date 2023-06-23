class NewsapiTextModel(object):
    def __init__(self, config, top_headlines):
        self.limit = config.video_editor.text_gen.limit
        self.en_text = []
        self.en_subtitle = []

        idx = 0
        for news in top_headlines['articles']:
            if idx == self.limit:
                break

            if news['description'] is None or news['content'] is None or news['urlToImage'] is None:
                continue
            
            if news['description'] == '' or news['content'] == '' or news['urlToImage'] == '':
                continue
            
            self.en_text.append(news['description'])
            self.en_subtitle.append(news['title'].rsplit('-')[0].strip())
            idx += 1
    
    def run(self,input_text):
        resp = {
            'lang':'en',
            'out_text':[],
            'out_subtitle':[]
        }
        for en_t in self.en_text:
            resp['out_text'].append({
                'en':en_t
            })
        for en_sub in self.en_subtitle:
            resp['out_subtitle'].append({
                'en':en_sub
            })
        return resp
