import os
from peewee import *

arq = "SistemaEspacial.db"
db = SqliteDatabase(arq)


class BaseModel(Model):
    class Meta:
        database = db


class Jogador (BaseModel):

    nome = CharField ()
    idade = CharField ()

    def __str__(self):
        return self.nome + self.idade


class Penalidade (BaseModel):

    numero_de_partidas = CharField()
    nivel_gravidade = CharField ()

    def __str__(self):

        return self. numero_de_partidas + self.nivel_gravidade

class Campeonato (BaseModel):

    nome = CharField ()
    nivel = CharField ()
    premio = ForeignKeyField (Premio)

    def __str__(self):
    
        return self.nome + self.nivel + self.premio

class Round (BaseModel):

    tempo = CharField()
    numero = CharField()

    def __str__(self):
        return self.tempo + self.numero

class Partida (BaseModel):

    narrador = ForeignKeyField (Narrador)
    rounds = ForeignKeyField (Round)
    times = ForeignKeyField (Time)
    jogadores = ForeignKeyField (Jogador)
    pausa = ForeignKeyField (Pause)
    data = CharField ()

    def __str__(self):

        return self.narrador + self.rounds + self.times + self.jogadores + self.pausa + self.data
    

class Narrador (BaseModel):

    nome = CharField ()
    lingua = CharField()

    def __str__(self):

        return self.nome + self.lingua

class Tecnico (BaseModel):

    nome = CharField ()


    def __str__(self):

        return self.nome + self.time

class Premio (BaseModel):

    campeoes = CharField()
    vice_campeoes = CharField()

    def __str__(self):

        return self.campeões + self.vice_campeoes

class Pause (BaseModel):

    motivo = CharField ()
    tempo = CharField()

    def __str__(self):

        return self.motivo + self.tempo

class Time (BaseModel):

    jogadores = ForeignKeyField (Jogador)
    tecnico = ForeignKeyField (Tecnico)
    nacionalidade = CharField ()

    def __str__(self): 

        return self.jogadores + self.tecnico + self.nacionalidade

if __name__ == "__main__":
    
    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Time,
                          Jogador,
                          Penalidade,
                          Campeonato,
                          Round,
                          Partida,
                          Narrador,
                          Tecnico, 
                          Premio,
                          Pause,])
    
    except OperationalError as e:
        print('erros: ' + str(e))

    jogador1 = Jogador.create (nome = Ramos, idade = 18)
    penalidade1 = Penalidade.create (numero_de_partidas = duas, nivel_penalidade = média)
    premio1 = Premio.create (campeoes = doze milhoes , vice_campeoes = cinco milhoes)
    campeonato1 = Campeonato.create (nome = superliga , nivel = nacional , premio = premio1)
    round1 = Round.create (tempo = 2 mins , numero = três)
    tecnico1 = Tecnico.create (nome = Hylson)
    time1 = Time.create (jogadores = jogador1 , tecnico = tecnico1 , nacionalidade = brasileiro)
    pausa1 = Pause.create (motivo = problemas tecnicos , tempo = 5 minutos)
    narrador1 = Narrador.create (nome = sérgio , lingua = portugues )
    partida1 = Partida.create (narrador = narrador1, rounds = round1 , times = time1 , jogadores = jogador1 , pausa=pausa1 , data = 20/5/2019)

    print (partida1)
    print ("")
    print (campeonato1)
    print ("")
    print (penalidade1)
