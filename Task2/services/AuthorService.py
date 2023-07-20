from typing import List

from sqlalchemy import select, update, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from Task2.models import Author


class AuthorService:

    async def get_by_id(self, session: AsyncSession, id: int):
        book = await session.scalars(select(Author).where(Author.id == id))
        return book.one()

    async def get_author_filter(self, session: AsyncSession, name: str, last_name: str = None):
        stmt = select(Author).where(Author.name.like(f'%{name}%'))
        if last_name:
            stmt = stmt.where(Author.last_name.like(f'%{last_name}%'))
        authors = await session.scalars(stmt)
        return authors.all()

    async def insert_authors(self, session: AsyncSession, books: List[dict]):
        await session.execute(insert(Author), books)
        await session.commit()

    async def update_author(self, session: AsyncSession, id: int, **kwargs):
        await session.execute(update(Author).where(Author.id == id), kwargs)
        await session.commit()

    async def delete_author(self, session: AsyncSession, id: int):
        await session.execute(delete(Author).where(Author.id == id))
        await session.commit()
