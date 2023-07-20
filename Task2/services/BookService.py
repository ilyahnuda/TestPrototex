from typing import List

from sqlalchemy import select, update, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from Task2.models import Book


class BookService:

    async def get_by_id(self, session: AsyncSession, id: int):
        book = await session.scalars(select(Book).where(Book.id == id))
        return book.one()

    async def get_books_filter(self, session: AsyncSession, name: str = ''):
        books = await session.scalars(select(Book).where(Book.name.like(f'%{name}%')))
        return books.all()

    async def insert_books(self, session: AsyncSession, books: List[dict]):
        await session.execute(insert(Book), books)
        await session.commit()

    async def update_book(self, session: AsyncSession, id: int, **kwargs):
        await session.execute(update(Book).where(Book.id == id), kwargs)
        await session.commit()

    async def delete_book(self, session: AsyncSession, id: int):
        await session.execute(delete(Book).where(Book.id == id))
        await session.commit()
