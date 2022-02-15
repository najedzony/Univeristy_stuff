import argparse
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:///data_base.db', echo = True)
Session = sessionmaker(bind = engine)

"""
Tworzę 2 klasy, jedna będzie trzymać opis filmu, a druga informacje o ludziach pracujących przy tym filmie. Mamy tutaj związek FilmDescription -> FilmPeople typu
one to many. Oczywiście ludzie pracujący przy filmie nie mogą istnieć bez filmu przy którym pracują, dlatego jeśli chcemy dodać jakiś rekord do FilmPeople, to musimy
podać także tytuł filmu, przy którym pracowali. Kiedy wypisuję tabelę FilmPeople, to wypisuję po prostu ludzi i film przy którym pracowali, rekord po rekordzie.
Gdy wypisuję tabelę FilmDescription to wypisuję wiersz tej tabeli i listę rekordów z tabeli FilmPeople, którzy odpowiadają id tego filmu.
"""

class FilmDescription(Base):
    __tablename__ = 'FilmDescription'

    id = Column(Integer, primary_key = True)
    title = Column(String(50), nullable=False)
    year = Column(Integer)
    people = relationship('FilmPeople')


class FilmPeople(Base):
    __tablename__ = 'FilmPeople'

    id = Column(Integer, primary_key = True)
    director = Column(String(50))
    operator = Column(String(50))
    producer = Column(String(50))

    description_id = Column(Integer, ForeignKey("FilmDescription.id"))

Base.metadata.create_all(engine)

parser = argparse.ArgumentParser()
parser.add_argument("name", help = "Use 'desciption' if u want to add something to 'FilmDescription' table or use 'people' if u want to add something to 'FilmPeople' table. Note that u can't add people working of the film, before adding a film description")
parser.add_argument("--title", help = "Title of a film")
parser.add_argument("--year", help = "A year in which film was shot")
parser.add_argument("--director", help = "Director of a film")
parser.add_argument("--operator", help = "Operator of a film")
parser.add_argument("--producer", help = "Producer of a film")
parser.add_argument("--dodaj", action='store_true', help = "Use it if u want to add something to the db. If you want to add something to FilmPeople you need to tell the title of the film aswell")
parser.add_argument("--wypisz", action='store_true', help = "Use it if u want to print the db.")

args = parser.parse_args()

sesja = Session()

if args.name == 'description':
    if args.dodaj: 
        o = FilmDescription(title = args.title, year = args.year)
        sesja.add(o)
        sesja.commit()
    elif args.wypisz:
        ans = []
        lista = sesja.query(FilmDescription).all()
        for i in lista:
            pom_lista = []
            for j in i.people:
                pom_lista.append((j.director, j.operator, j.producer))
            if len(pom_lista):
                ans.append((i.id, i.title, i.year, pom_lista))
            else:
                ans.append((i.id, i.title, i.year))
        print()
        print('Tabela z opisem filmów:')
        for i in ans:
            print(i)
elif args.name == 'people':
    if args.dodaj:
        lista = sesja.query(FilmDescription).filter(FilmDescription.title == args.title).all()
        o = FilmPeople(director = args.director, operator = args.operator, producer = args.producer, description_id = lista[0].id)
        sesja.add(o)
        lista[0].people.append(o)
        sesja.commit()
    elif args.wypisz:
        ans = []
        lista = sesja.query(FilmPeople).all()
        for i in lista:
            pom_lista = sesja.query(FilmDescription).filter(FilmDescription.id == i.description_id)
            ans.append((i.id, i.director, i.operator, i.producer, pom_lista[0].title, pom_lista[0].year))
        print()
        print('Tabela z ludźmi biorącymi udział przy danym filmie')
        for i in ans:
            print(i)



