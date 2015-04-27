__author__ = 'Giovanni'

tagli = [.1, .2, .5, 1, 2]

class RestoMat(object):
    def __init__(self, capienze=[]):
        """
        Inizializza la classe riempiendo i vari slot cei tagli con i numeri di monete corrispondenti
        :param capienze: lista nella forma [x,x,x] deve essere lunga esattamente come la lista dei tagli
        :return:
        """
        self.tagli = tagli
        self.tagli.reverse()
        self.capienze = capienze
        self.capienze.reverse()
        self.attivo = True
        if len(self.tagli) != len(self.capienze):
            self.attivo = False

    def slotEsaurito(self, taglio):
        """
        Ritorna True se lo slot contenente le monete del taglio richiesto ha esaurito le monete
        :param taglio: numerico contenente il taglio da esaminare
        :return: True se le monete sono esaurite, False altrimenti.
        """
        if taglio in self.tagli:
            if self.capienze[self.tagli.index(taglio)] == 0:
                return True
            else:
                return False

    def calcolaResto(self, prezzo, importo):
        """
        Calcola il resto da corrispondere per il dato prezzo e il dato importo inserito
        :param prezzo: numerico. Il prezzo da pagare
        :param importo: numerico. L'importo versato in monete
        :return: float. L'ammontare del resto
        """
        return float(importo) - float(prezzo)

    def erogaResto(self, prezzo, importo):
        """
        Ritorna una lista contenente il numero di monete da erogare in relazione al taglio
        :param prezzo: numerico. Il prezzo da pagare
        :param importo: numerico. L'importo versato in monete
        :return: lista di interi
        """
        progressivo = 0
        daErogare = self.calcolaResto(prezzo, importo)
        monete = [0] * len(self.tagli)
        for i in range(0, len(self.tagli)):
            while (progressivo + self.tagli[i]) <= daErogare:
                if self.slotEsaurito(self.tagli[i]):
                    break
                else:
                    progressivo += self.tagli[i]
                    monete[i] += 1
                    self.capienze[i] -= 1
        monete.reverse()
        return monete

foo = RestoMat([5,5,5,5,5])
print foo.erogaResto(2.6,3)
tagli.reverse()
print tagli
