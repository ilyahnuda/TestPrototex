from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import date
from sqlalchemy import DATE, Column, Integer


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = 'book'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[date] = mapped_column(DATE)
    price: Mapped[float]
    language: Mapped[str]


class Author(Base):
    __tablename__ = 'author'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str]
    age: Mapped[int] = mapped_column(nullable=False)


class BookAuthor(Base):
    __tablename__ = 'book_author'

    author_id = Column(Integer, ForeignKey('author.id'), primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
