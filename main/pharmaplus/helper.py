from .models import *
from random import randint



def cleaner(x):
    # print("X:", x)
    ls = x.split('\t')
    med = ls[0].strip('\n')
    store_id = ls[1].strip('\n')

    medicine = Medicine.objects.get(name = med)
    store = Stores.objects.get(id = store_id)
    quantity = randint(50,100)

    dc = {
        "medicine" : medicine,
        "store" : store,
        "quantity" : quantity
    }

    return dc

    


def modelSaver(dc):
    ob = Availability(medicine = dc['medicine'], store = dc['store'], quantity = dc['quantity'])
    ob.save()


with open("/home/anshul/Desktop/itw/Table2.txt") as f:
    raw = f.readlines()
    for i in raw:
        print(i)
        modelSaver(cleaner(i))




# if __name__ == "__main__":
#     main()

