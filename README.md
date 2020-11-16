repo wymiany sql do bazy danych

FLOW:
    0. account_unlock.sql - w razie zablokowanie konta (odpalić z SYS)
    1. link_creation.sql - utworzyć na każdym serwerze dla każdego z pozostałych serwerów
    2. positions.sql - odpalić na każdym serwerze (najpierw dopisać linki)
    3. locations_init.sql - odpalić na każdym serwerze (najpierw zmienić nazwę miasta i id)
    4. locations_snapshots.sql - odpalić na każdym serwerze (najpierw dopisać linki)
    5. insurers_init.sql - odpalić na każdym serwerze
    6. insurers_snapshots.sql - odpalić na każdym serwerze (najpierw dopisać linki)
    7. workers_init.sql - odapalić na każdym serwerze (najpierw dopisać linki)
    8. workers_triggers.sql - odpalić na każdym serwerze każdy trigger oddzielnie (najpierw dopisać linki i pozmieniać warunki)
    9. <to co ty wysłałeś - preferences i relations>
    11.insurances.sql - odpalić na każdym serwerze stosowną część (opis wewnątrz)
    