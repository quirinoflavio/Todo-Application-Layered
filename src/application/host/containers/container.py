from dependency_injector import containers, providers

from src.application.host.containers.domain_service import (
    DomainServiceContainer,
)
from src.application.host.containers.repository import RepositoryContainer


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.application.services.todo_lists.todo_list_appservice",
        ]
    )

    repositories: RepositoryContainer = providers.Container(
        RepositoryContainer
    )

    managers: DomainServiceContainer = providers.Container(
        DomainServiceContainer,
        todo_list_repository=repositories.todo_list_repository,
    )
