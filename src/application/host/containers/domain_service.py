from dependency_injector import containers, providers

from domain.todo_lists.todo_list_manager import TodoListManager


class DomainServiceContainer(containers.DeclarativeContainer):
    todo_list_repository = providers.Dependency()

    todo_list_manager = providers.Factory(
        TodoListManager,
        todo_list_repository=todo_list_repository,
    )
