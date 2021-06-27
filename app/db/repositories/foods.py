from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository


class FoodsRepository(BaseRepository): 
    async def create_food(  # noqa: WPS211
        self,
        *,
        name: str,
    ) -> Food:
        async with self.connection.transaction():
            food_row = await queries.create_new_article(
                self.connection,
                slug=slug,
                title=title,
                description=description,
                body=body,
                author_username=author.username,
            )

            if tags:
                await self._tags_repo.create_tags_that_dont_exist(tags=tags)
                await self._link_article_with_tags(slug=slug, tags=tags)

        return await self._get_article_from_db_record(
            article_row=article_row,
            slug=slug,
            author_username=article_row[AUTHOR_USERNAME_ALIAS],
            requested_user=author,
        )