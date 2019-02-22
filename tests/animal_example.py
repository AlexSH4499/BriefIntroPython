from animals import *

def sample_mammal():
    dog = Mammal(name="Cannis familiaris", diet="Omnivorous",  schedule="Diurnal")
    return dog

def sample_amphibian():
    frog= Amphibian(name="Eleutherodactylus portoricensis",diet="Omnivorous", schedule="Nocturnal")
    return frog


def to_file(filename, data):
    try:
        with open(filename, 'wt') as f:
            f.write(data)
    except FileExistsError as e:
        print(e)

if __name__== "__main__":
    dog = str(sample_mammal())
    frog = str(sample_amphibian())
    to_file(filename="sample.txt", data=dog+frog)
