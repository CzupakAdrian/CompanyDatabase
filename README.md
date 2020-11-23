Rozproszona baza danych

W folderze Database/ znajdują się pliki sql służące do postawienia bazy danych.
W folderze App/ zandjuje się projekt aplikacji python.
Poniżej przedstawiono sposób postępowania w celu bezawaryjnej generacji bazy danych.

FLOW:

0. account_unlock.sql - w razie zablokowanie konta (odpalić z SYS)
1. link_creation.sql - utworzyć na każdym serwerze dla każdego z pozostałych serwerów
2. positions.sql - odpalić na każdym serwerze (najpierw dopisać linki)
3. locations_init.sql - odpalić na każdym serwerze (najpierw zmienić nazwę miasta i id)
4. locations_snapshots.sql - odpalić na każdym serwerze (najpierw dopisać linki)
5. insurers.sql - odpalić wg komentarza
6. workers_init.sql - odapalić na każdym serwerze (najpierw dopisać linki)
7. workers_triggers.sql - odpalić na każdym serwerze każdy trigger oddzielnie (najpierw dopisać linki i pozmieniać warunki)
8. relations - na każdym serwerze
9. workers_preferences.sql - na każdym serwerze
10. insurances.sql - odpalić na każdym serwerze stosowną część (opis wewnątrz)

11. Odpalić DbInit.py na jednym z serwerów w celu wstawienia
losowych danych (w razie potrzeby zakomentować niepotrzebne assercje)
