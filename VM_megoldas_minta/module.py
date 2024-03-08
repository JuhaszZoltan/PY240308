class Termek:
    def __init__(self, sor:str) -> None:
        v:list[str] = sor.strip().split(';')
        self.kod:str = v[0]
        self.nev:str = v[1]
        self.ar:int = int(v[2])
        self.keszlet:int = int(v[3])
        w:list[str] = self.nev.split(' ')
        self.kiszereles:int = int(w[-2].replace('(', ''))