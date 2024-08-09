from datetime import date
from io import BytesIO

import requests

from src.core.config import settings
from src.core.media import MediaRepository
from src.enums.auth import Role
from src.exceptions.services import NotFoundException, NoRightsException, ServerError
from src.models.auth import User, ArtistProfile, ProducerProfile
from src.repositories.auth import UsersDAO, ArtistDAO, ProducerDAO, RoleDAO, UserToRoleDAO
from src.repositories.tags import ListenerTagsDAO, TagsDAO
from src.utils.auth import create_access_token, create_refresh_token, get_hashed_password


class AuthService:
    @staticmethod
    async def get_user_by_id(user_id: int) -> User:
        user = await UsersDAO.find_one_by_id(id_=user_id)

        if not user:
            raise NotFoundException()

        return user

    @staticmethod
    async def get_all_users() -> list[User]:
        return await UsersDAO.find_all()

    @staticmethod
    async def update_current_user_picture(
        file_stream: BytesIO,
        file_info: str | None,
        user_id: int
    ) -> None:

        user = await UsersDAO.find_one_by_id(id_=user_id)

        if not user:
            raise NotFoundException()

        picture_url = await MediaRepository.upload_file("PICTURES", file_info, file_stream)

        update_data = {"picture_url": picture_url}
        await UsersDAO.edit_one(user_id, update_data)

    @staticmethod
    async def update_current_user(
        name: str | None,
        username: str | None,
        picture_url: str | None,
        description: str | None,
        user_id: int
    ) -> dict[str, str]:
        user = await UsersDAO.find_one_by_id(id_=user_id)

        if not user:
            raise NotFoundException()

        update_data = dict()

        if username:
            update_data["username"] = username
        if picture_url:
            update_data["picture_url"] = picture_url
        if name:
            update_data["name"] = picture_url
        if description:
            update_data["description"] = description

        await UsersDAO.edit_one(user_id, update_data)
        return update_data

    @staticmethod
    async def delete_current_user(user_id: int) -> None:
        user = await UsersDAO.find_one_by_id(id_=user_id)

        if not user:
            raise NotFoundException()

        await UsersDAO.delete(user_id)

    @staticmethod
    async def get_artist_by_id(artist_id: int) -> ArtistProfile:
        artist = await ArtistDAO.find_one_by_id(id_=artist_id)

        if not artist:
            raise NotFoundException()

        return artist

    @staticmethod
    async def get_all_artists() -> list[ArtistProfile]:
        return await ArtistDAO.find_all()

    @staticmethod
    async def update_current_artist(artist_id: int, description: str) -> None:
        artist = await ArtistDAO.find_one_by_id(id_=artist_id)

        if not artist:
            raise NotFoundException()

        update_data = {"description": description}
        await UsersDAO.edit_one(artist_id, update_data)

    @staticmethod
    async def deactivate_artist(artist_id: int) -> None:
        artist = await ArtistDAO.find_one_by_id(id_=artist_id)

        if not artist:
            raise NotFoundException()

        await ArtistDAO.delete(artist_id)

    @staticmethod
    async def get_producer_by_id(producer_id: int) -> ProducerProfile:
        producer = await ProducerDAO.find_one_by_id(id_=producer_id)

        if not producer:
            raise NotFoundException()

        return producer

    @staticmethod
    async def get_all_producers() -> list[ProducerProfile]:
        return await ProducerDAO.find_all()

    @staticmethod
    async def update_one_producer(producer_id: int, description: str) -> None:
        producer = await ProducerDAO.find_one_by_id(id_=producer_id)

        if not producer:
            raise NotFoundException()

        update_data = {"description": description}
        await UsersDAO.edit_one(producer_id, update_data)

    @staticmethod
    async def deactivate_one_producer(producer_id: int) -> None:
        producer = await ProducerDAO.find_one_by_id(id_=producer_id)

        if not producer:
            raise NotFoundException()

        await ArtistDAO.edit_one(producer_id, {"is_available": False})

    @staticmethod
    async def create_new_user(
        username: str,
        password: str,
        email: str,
        roles: list[Role],
        birthday: date | None,
        tags: list[str] | None
    ) -> None:
        existing_user = await UsersDAO.find_one_or_none(email=email)
        if existing_user:
            raise NoRightsException()

        role_superuser = await RoleDAO.find_one_by_id(id_=1)

        if not role_superuser:
            pass

        user_roles = list()

        for role_name in roles:
            role = await RoleDAO.find_one_or_none(name=role_name)
            if role:
                user_roles.append(role)
            else:
                raise NotFoundException("Role not found")

        user_tags = list()

        for tag_name in tags:
            tag = await TagsDAO.find_one_or_none(name=tag_name)

            if tag:
                user_tags.append(tag)
            else:
                raise NotFoundException("Role not found")

        hashed_password = get_hashed_password(password)

        user = await UsersDAO.add_one(
            {
                "username": username,
                "email": email,
                "password": hashed_password,
                "birthday": birthday,
            }
        )

        for tag in user_roles:
            await ListenerTagsDAO.add_one({"user_id": user.id, "tag_id": tag.id})

        for role in user_roles:
            await UserToRoleDAO.add_one({"user_id": user.id, "role_id": role.id})

        artist_profile_id = await ArtistDAO.add_one({"description": "Hi, I'm an artist"})
        await UsersDAO.edit_one(user.id, {"artist_profile_id": artist_profile_id})
        await ProducerDAO.edit_one(artist_profile_id, {"is_available": False})

        producer_profile_id = await ProducerDAO.add_one(
            {"description": "Hi, I'm a producer"}
        )
        await UsersDAO.edit_one(user.id, {"producer_profile_id": producer_profile_id})
        await ArtistDAO.edit_one(user.id, {"is_available": False})

    @staticmethod
    async def login(user: User) -> tuple[str, str]:

        access_token = create_access_token({"sub": str(user.id)})
        refresh_token_ = create_refresh_token({"sub": str(user.id)})

        return access_token, refresh_token_

    @staticmethod
    async def refresh_token(user_id: int) -> tuple[str, str]:

        access_token = create_access_token({"sub": str(user_id)})
        refresh_token_ = create_refresh_token({"sub": str(user_id)})

        return access_token, refresh_token_

    @staticmethod
    async def spotify_callback(code) -> tuple[str, str]:
        payload = {
            "code": code,
            "client_id": settings.spotify.CLIENT_ID,
            "client_secret": settings.spotify.CLIENT_SECRET,
            "grant_type": "authorization_code",
            "redirect_uri": "http://localhost:5173/profile",
        }

        auth_response = requests.post(
            url="https://accounts.spotify.com/api/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=payload,
        )
        auth_response_data = auth_response.json()

        access_token = auth_response_data.get("access_token")

        if access_token:
            user_response = requests.get(
                "https://api.spotify.com/v1/me",
                headers={"Authorization": f"Bearer {access_token}"},
            )
            user_data = user_response.json()

            user = await UsersDAO.find_one_or_none(email=user_data.get("email"))
            if not user:
                new_user = {
                    "id": user_data["id"],
                    "username": user_data.get("username"),
                    "email": user_data.get("email"),
                    "password": None,
                }

                await UsersDAO.add_one(new_user)
                user = new_user
                access_token = create_access_token({"sub": str(user["id"])})
                refresh_token_ = create_refresh_token({"sub": str(user["id"])})

                return access_token, refresh_token_

            else:
                access_token = create_access_token({"sub": str(user.id)})
                refresh_token_ = create_refresh_token({"sub": str(user.id)})

                return access_token, refresh_token_

        else:
            raise ServerError("Failed to obtain access token")
