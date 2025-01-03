from dataclasses import dataclass

from swarmnode._client import Client
from swarmnode.pagination import PagePaginatedResource
from swarmnode.resources._base import Resource
from swarmnode.types import JSON


@dataclass
class Store(Resource):
    id: str
    name: str
    data: JSON
    created: str

    @classmethod
    def api_source(cls):
        return "stores"

    @classmethod
    def list(cls, page: int = 1, page_size: int = 3) -> PagePaginatedResource["Store"]:
        params = {"page": page, "page_size": page_size}
        r = Client.request_action("GET", f"{cls.api_source()}/", params=params)
        return PagePaginatedResource(
            _next_url=r.json()["next"],
            _previous_url=r.json()["previous"],
            _resource_class=cls,
            total_count=r.json()["total_count"],
            current_page=r.json()["current_page"],
            results=[cls(**result) for result in r.json()["results"]],
        )

    @classmethod
    def retrieve(cls, id: str) -> "Store":
        r = Client.request_action("GET", f"{cls.api_source()}/{id}/")
        return cls(**r.json())

    @classmethod
    def create(cls, name: str) -> "Store":
        r = Client.request_action(
            "POST", f"{cls.api_source()}/create/", data={"name": name}
        )
        return cls(**r.json())

    @classmethod
    def update(cls, id: str, **kwargs) -> "Store":
        """
        The following fields can be updated: `name`.
        """

        r = Client.request_action(
            "PATCH", f"{cls.api_source()}/{id}/update/", data=kwargs
        )
        return cls(**r.json())

    @classmethod
    def delete(cls, id: str) -> None:
        Client.request_action("DELETE", f"{cls.api_source()}/{id}/delete/")
