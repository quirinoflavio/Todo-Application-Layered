# Todo Application - Layered Solution

## Project Structure
```
+---.vscode
+---src
|   +---application
|   |   +---contracts
|   |   |   +---exceptions
|   |   |   |   +---authentication
|   |   |   |   +---http_400
|   |   |   |   \---http_500
|   |   |   +---tasks
|   |   |   |   +---dtos
|   |   |   |   \---mapping
|   |   |   \---todo_lists
|   |   |       +---dtos
|   |   |       \---mapping
|   |   +---host
|   |   |   +---api
|   |   |   |   \---object_mapper
|   |   |   +---containers
|   |   |   \---middlewares
|   |   |       \---exception_handlers
|   |   \---services
|   |       \---todo_lists
|   +---core
|   |   +---dtos
|   |   +---entities
|   |   +---exceptions
|   |   +---mapper
|   |   \---services
|   |       +---application
|   |       \---domain
|   +---domain
|   |   +---tasks
|   |   +---todo_lists
|   |   \---users
|   \---infrastructure
|       +---external
|       \---sqlalchemy
|           +---core
|           |   +---entities
|           |   \---utils
|           +---mapping
|           +---models
|           |   +---tasks
|           |   +---todo_lists
|           |   \---users
|           \---repositories
|               \---todo_lists
\---tests
    +---application
    |   \---services
    |       \---todol_ists
    \---utils
        \---factories
            \---todo_lists
```
