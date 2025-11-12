from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "sqlite:///relacoes.db"
engine = create_engine(DATABASE_URL, echo=True, future=True)

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, future=True)

print('feito com sucesso')

# Modelos

class Loja(Base):
    __tablename__ = "lojas"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)
    gerente = Column(String, nullable=False)

    vendedores = relationship("Vendedor", back_populates="loja")

class Vendedor(Base):
    __tablename__ = "vendedores"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=True)

    loja_id = Column(Integer, ForeignKey("lojas.id"))
    loja = relationship("Loja", back_populates="vendedores")

    vendas = relationship("Venda", back_populates="vendedor")

class Venda(Base):
    __tablename__ = "vendas"
    id = Column(Integer, primary_key=True)
    carro = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    comissao = Column(Float)

    vendedor_id = Column(Integer, ForeignKey("vendedores.id"))
    vendedor = relationship("Vendedor", back_populates="vendas")

# Criando as tabelas
Base.metadata.create_all(engine)

# Criando uma sessão (exemplo)
session = SessionLocal()
