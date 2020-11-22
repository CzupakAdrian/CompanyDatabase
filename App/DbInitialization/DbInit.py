import time
from orm_controllers.DbConnection import DbConnectionAdrianSarajevo
from Test.TablesController import TablesController
import datetime


def wait_for_refresh(seconds):
    print(f'Waiting {seconds}s for refresh ', end='')
    for i in range(seconds + 1):
        print('.', end='')
        time.sleep(1)


def init_insurers(controller):
    if not controller.insurers.get_all():
        print("insurers table is empty: add first one manually")
        return False
    else:
        if controller.insurers.get_all().count() == 1:
            controller.insurers.init()
            print("insurers initialized")
        else:
            print("insurers already initialized")
        return True


def init_locations(controller):
    if not controller.locations.get_all():
        print("basic insurers not added")
        return False
    else:
        print("insurers already initialized")
        return True


def init_insurances(controller):
    #odkomentuj wszystko tu, bo u mnie są połączenia i nie mogłem tego zrobić
    if not controller.insurances.get_all():
        #controller.insurances.delete_all()
        print("insurances deleted for initialization")
        controller.insurances.add_insurance(1, 1, datetime.date.fromisoformat("2023-12-12"))

    #controller.insurances.add_random()
    print("insurances initialized")
    return True


def init_positions(controller):
    if not controller.positions.get_all():
        print("positions table is empty: add manually [1, 'Boss'] in each location")
        return False
    elif controller.positions.get_all().count() == 1:
        controller.positions.add_position("Developer")
        controller.positions.add_position("Scrum Master")
        controller.positions.add_position("Chef")
        controller.positions.add_position("Waiter")
        controller.positions.add_position("Tester")
        print("positions initialized")
    else:
        print("positions already initialized")
    return True


def init_workers(controller):
    if not controller.workers.get_all():
       print("workers table is empty: add one manually in one location")
       return False

    elif controller.workers.get_all().count() == 1:
        controller.workers.add_random()
        print("workers initialized")
    else:
       print("workers already initialized")
    return True


def init_preferences(controller):
    if controller.preferences.get_all().count() < 10:
        controller.preferences.add_random()
        print("preferences initialized")
    else:
        print("preferences already initialized")
    return True


if __name__ == "__main__":
    controller = TablesController(DbConnectionAdrianSarajevo())
    assert init_insurers(controller)
    assert init_locations(controller)
    assert init_insurances(controller)
    assert init_positions(controller)
    assert init_workers(controller)
    assert init_preferences(controller)
