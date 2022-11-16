from abc import ABC, abstractmethod

class Magic(ABC):
    def words(self, word):
        print("Abra-", word)
    @abstractmethod
    def letters(self,word):
        pass
class MoreMagic(Magic):
    def letters(self,word):
        print("Did {} work?".format(word))

obj = MoreMagic()
obj.words("ka-da-bra")
obj.letters("qwerty")
