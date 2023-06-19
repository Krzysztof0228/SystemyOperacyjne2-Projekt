# SystemyOperacyjne2-Projekt

## Opis projektu

## Wizualizacja

![Alt text](image.png)

1. Listowanie okrążeń

2. Przejechanie wszystkich okrążeń

3. Wyniki

## Coś tam

* Wątki i co reprezentują
W programie znajduje się 20 wątków, które reprezentują samochody biąrące udział w wyścigu, kążdy samochód ma przydzielony numer od 1 do 20. Wątki ścigają się o dostęp do sekcji krytycznej. Liczba udanych dostępów do sekcji krytycznej oznacza liczbę pokonanych przez dany samochód okrążęń.

* Sekcje krytyczne
O dostęp do niej ścigają się wątki reprezentujące samochody. W danym momencie dostęp do sekcji krytycznej ma tylko jeden wątek. Zaimplementowana sekcja krytyczna używa muteksu, czyli blokady, która jest potrzebna do synchonizacji dostępu do sekcji krytycznej.