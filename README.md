# PESEL reader
## Program służy do odczytywania danych z numeru PESEL.
Powstał jako projekt zaliczeniowy z przedmiotu Języki Skryptowe.

## Opis działania:
Na początku program wczytuje wszystkie podane w pliku tekstowym numery PESEL i sprawdza ich poprawność(czy mają odpowiednią ilość cyfr, czy składa się jedynie z cyfr i czy cyfra kontrolna się zgadza, czy data urodzenia jest późniejsza niż obecna data). Następnie program poprzez sprawdzenie odpowiednich cyfr numeru odczytuje płeć i datę urodzenia osoby o podanym numerze PESEL i sortuje numery od najstarszego do najmłodszego, dzięki algorytmowi sortowania bąbelkowego. Na koniec program może zapisać posortowane dane do nowego pliku.

## Dane wejściowe:
Program obsługuje pliki w formacie .txt. Plik powinien zawierać wyłącznie numery PESEL, każdy jeden w osobnej linii, bez żadnych znaków interpunkcyjnych (patrz plik: “plik_czysty.txt”). Oczywiście program posiada obsługę błędów, ale żeby dane zostały poprawnie przetworzone należy zadbać o poprawność pliku wejściowego.

## Wyniki działania: 
Wyniki działania są wyświetlane w oknie programu w postaci listy przewijanej. Jest także możliwość zapisu wyników do pliku. W tym celu należy wcisnąć przycisk zapisz i wybrać lokalizację zapisu. Plik jest zapisywany w formacie txt.
