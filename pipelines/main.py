from numpy import argsort
from transformers import pipeline
from pipelines.vocabs.words import words
import random

class CompletionsWithPredictionWithSentsPipeline(object): # This will become
    def __init__(self):
        self.pos_words = [s.lower() for s in words['neu']+words['pos']]
        self.neg_words = [s.lower() for s in words['neu']+words['neg']]
        pipe_spec = {
            'model': 'distilbert-base-uncased',
            'topk':20,
        }
        self.pipe = pipeline('fill-mask', **pipe_spec)
        self.mask = self.pipe.tokenizer.mask_token

    def get_suggestions(self, text, group):
        if(group=='1'):
            return(self._get_completions(text,self.pos_words))
        elif(group=='-1'):
            return(self._get_completions(text,self.neg_words))
        else:
            if(random.sample(['1','-1'], 1)=='1'):
                self._get_completions(text,self.pos_words)
            else:
                self._get_completions(text,self.neg_words)
            return(['','',''])

    def _get_completions(self, text, words):
        if(text==''):
            return([s.capitalize() for s in words[:3]])
        elif(text[-1]!=' '):
            currentWord = text.rsplit(' ', 1)[-1]
            isCapitalised = False if currentWord=='' else currentWord[0].isupper()
            valid = [w for w in words if w.startswith(currentWord.lower())]
            if(isCapitalised):
                valid = [s.capitalize() for s in valid]
            if(len(valid)<3):
                valid += ['']*(3 - len(valid))
            return(valid[:3])
        else:
            text = text.rsplit('.', 1)[-1].lstrip()
            if(text==''):
                return([s.capitalize() for s in words[:3]])
            else:
                masked_text = f'{text.strip()} {self.mask}.'
                valid = [s['token_str'] for s in self.pipe(masked_text) if not s['token_str'].startswith('##')]
                if(len(valid)<3):
                    valid += ['']*(3 - len(valid))
                return(valid[:3])
