from character_base import Player

def save(character):
    # file=open("load.txt", "a")
    saving = list()
    with open("load.txt", "w") as file:
        for attribute in character.__dict__.items():
            saving.append(str(attribute))
        for item in saving:
            file.write(item + "\n")
    # file.close()

def load():
    loading = list()
    with open("load.txt", "r") as file:
        for line in file:
            loading.append(line)
            print(line)
    print(loading)