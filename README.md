Opis dzialania aplikacji:
Aplikacja składa się z następujących komponentów:
--- Skrypt pobiera dane z API OpenWeather za pomocą pliku JSON 
--- Skrypt nr 2 tworzy baze SQLLite za pomocą frameworka SQLAlcehmy 
--- Dane z tabeli są ładowane codziennie, tworzymym sobie aplikacja

Problemy z jakimi się mierzymy:
--- Pobranie danych za pomocą API przeczytać dokumentację API OpenWeather
--- Zaplanowanie odpowiedniej architektury bazy danych
--- Stworzenie bazy danych za pomocą SQLAlchemy 
--- Wrzucenie danych na serwer 

-- Lista kluczy dla pliku JSON
dict_keys(['coord', 'weather', 'base', 'main', 'visibility', 'wind', 'clouds', 'dt', 'sys', 'timezone', 'id', 'name', 'cod'])
('sys', {'type': 1, 'id': 1414, 'country': 'GB', 'sunrise': 1578816126, 'sunset': 1578845677}), ('timezone', 0), ('id', 2643743), ('name', 'London'), ('cod', 200)])
Tworzenie relacji w SQLAlchemy --- tutorial stworzyć relacje pomiędzy bazami Weather, City oraz Wind --- zadanie wtorek 2020-01-14:

Stan na dziś:
Skrypt z importem danych do bazy 
Skrypt z tworzeniem danych do bazy 

Co jeszcze potrzeba? 
Pobieranie danych codziennie i wgrywanie ich na bazę --- usunąc memory i stworzyć normalną bazę danych 
Stworzenie relacji za pomocą ORM --- 
Poprawa skryptów 
Napisanie testów -- uczę się testowanie danego projektu 
