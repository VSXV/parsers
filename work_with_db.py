from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, declared_attr


class Base:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Pep(Base):
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))

    def __repr__(self):
        return f"PEP {self.pep_number} {self.name}"


if __name__ == "__main__":
    engine = create_engine("sqlite:///sqlite.db", echo=False)

    session = Session(engine)

    results = session.query(Pep).all()
    print(results)
    results = session.query(Pep.name, Pep.status).first()
    print(results)
