class Jatekos:
    def __init__(self, s:str) -> None:
        v:list[str] = s.strip().split(';')
        self.mezszam:int = int(v[0])
        self.nev:str = v[1]
        self.nemzet:str = v[2]
        self.poszt:str = v[3]
        self.szulev:int = int(v[4])