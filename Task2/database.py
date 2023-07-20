from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import asyncio
from config import DB_USER, DB_PORT, DB_HOST, DB_NAME, DB_PASSWORD
from Task2.services.AuthorService import AuthorService

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def main():
    service = AuthorService()
    async with async_session() as session:
        # await service.insert_authors(session, [{'name': 'gf', 'age': 52, 'last_name': 'gfgf'}])
        # await service.update_author(session, 1, name='SARA')
        # await  service.delete_author(session, 1)
        res = await service.get_by_id(session, 2)
        res = await service.get_author_filter(session, name='gf',last_name='gfg')
        print(res)


if __name__ == '__main__':
    asyncio.run(main())
