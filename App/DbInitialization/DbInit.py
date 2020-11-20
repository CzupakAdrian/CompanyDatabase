import time
from orm_controllers.DbConnection import DbConnectionAdrianSarajevo
from orm_controllers.TablesController import TablesController


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
        print("basic locations not added")
        return False
    else:
        print("locations already initialized")


if __name__ == "__main__":
    controller = TablesController(DbConnectionAdrianSarajevo())
    assert init_insurers(controller)
    assert init_locations(controller)





