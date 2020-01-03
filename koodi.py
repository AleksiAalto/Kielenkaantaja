#from translate import Tranlator
# => ongelma translaten importtauksessa, en saa edes kierrettyä ja ladattua.
#testasin lataamalla muita lisäosia ja niissä ei ollut ongelmaa
#pitäisi latautua terminaalissa pip3 install translate
#lisätietoa translate lisäosasta: https://pypi.org/project/translate/

#kaantaja = Translator(to_lang="") #tänne kielilyhenne, lyhenteet: https://en.wikipedia.org/wiki/ISO_639-1
try:
    with open('./teksti.txt', mode='r') as teksti:
        text = teksti.read()
        kaannos = kaantaja.translate(text)
        with open('./teksti-.txt', mode='w') as teksti2: #lisäämällä viivan jälkeen lyhenne, millä kielellä
            teksti2.write(kaannos) #käännetty teksti. Ohjelma luo toisen txt tiedoston, jossa sama teksti,
                                    #mutta käännetty eri kielelle. Esim suosittelen nimeämään japanin kielisen tiedoston
                                    #teksti-ja.txt
except FileNotFoundError as e:
    print('Onko luettava tekstitiedosto olemassa samassa kansiossa?')