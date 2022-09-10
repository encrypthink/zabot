class String:
    def snake_to_camel(self, word):
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

    def string_to_list(self, word):
        return list(word.split("_"))