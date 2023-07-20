from typing import List

from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from Task2.models import BookAuthor


class BookAuthorService:

    async def get_books_filter(self, session: AsyncSession, **kwargs):
        stmt = select(BookAuthor)
        if 'author_id' in kwargs:
            stmt = stmt.where(BookAuthor.author_id == kwargs['author_id'])
        if 'book_id' in kwargs:
            stmt = stmt.where(BookAuthor.book_id == kwargs['book_id'])
        res = await session.scalars(stmt.join())
        return res.all()

    async def insert_row(self, session: AsyncSession, bookauthors: List[dict]):
        await session.execute(insert(BookAuthor), bookauthors)
        await session.commit()

    async def delete_book(self, session: AsyncSession, book_id: int, author_id: int):
        await session.execute(
            delete(BookAuthor).where(BookAuthor.book_id == book_id).where(BookAuthor.author_id == author_id))
        await session.commit()