import os
import pandas as pd

def zapisz_sciezki_do_excela(sciezka, nazwa_pliku_excel):

    pelne_sciezki = [os.path.join(os.path.abspath(sciezka), plik) for plik in os.listdir(sciezka)]


    dane = {
        'sciezka': [],
        'nazwa_pliku': []
    }
    
    for pelna_sciezka in pelne_sciezki:

        if os.path.isfile(pelna_sciezka):
            dane['sciezka'].append(pelna_sciezka)
            dane['nazwa_pliku'].append(os.path.basename(pelna_sciezka))

    df = pd.DataFrame(dane)
    
    df.to_excel(nazwa_pliku_excel, index=False)
    print(f'Pliki zapisane do {nazwa_pliku_excel}')


zapisz_sciezki_do_excela('.', 'lista_plikow.xlsx')
