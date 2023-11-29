#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value

    def get_value(self):
        self._value

    def set_value(self, value):
        if (type(value)== str):
            self._value = value
        else:
            print ("The value must be a string.")

    value = property(get_value, set_value)
        
    def is_sentence(self):
        return True if self._value.endswith('.') else False
    
    def is_question(self):
        return True if self._value.endswith('?') else False
    
    def is_exclamation(self):
        return True if self._value.endswith('!') else False
    
    def count_sentences(self):
        count = 0
        for sentence in self._value.split():
            if sentence.endswith('.') or sentence.endswith('!') or sentence.endswith('?'):
                count += 1
        return count
        
        

         

        
    

  
