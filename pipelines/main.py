class NorthPipeline(object):
    def __init__(self):
        self.firstWordSuggestions = ['The','I','This']

    def get_suggestions(self, text_data):
        # Extract the input text from the text_data
        input_text = text_data['input_text']

        # Text-based Router
        if(input_text==''):
            suggestions = self.firstWordSuggestions
        else:
            if('sentiment_bias' in text_data):
                if(text_data['sentiment_bias']=='1'):
                    suggestions = ['This','is','positive']
                elif(text_data['sentiment_bias']=='-1'):
                    suggestions = ['This','is','negative']
                else:
                    suggestions = ['','','']
            else:
                suggestions = ['','','']
        return({'suggestions': suggestions})

class TestRouterPipeline(object):
    def __init__(self):
        pass

    def get_suggestions(self, text_data):
        # Sometime generalise to more general routers
        if('sentiment_bias' in text_data):
            if(text_data['sentiment_bias']=='1'):
                suggestions = ['This','is','positive']
            elif(text_data['sentiment_bias']=='-1'):
                suggestions = ['This','is','negative']
            else:
                suggestions = ['','','']
        else:
            suggestions = ['','','']
        return({'suggestions': suggestions})


class TestPipeline(object):
    def __init__(self):
        pass

    def get_suggestions(self, text_data):
        return({'suggestions': ['This','is','Test']})
