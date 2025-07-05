# async-graphene-django
A drop-in extension for graphene-django that enables fully async GraphQL execution. This package provides an AsyncGraphQLView and integrates Django's async capabilities to support modern asynchronous resolvers, improving performance and compatibility with async-based backends.

## 中文文档

此项目提供 `AsyncGraphQLView`，用于將 `graphene-django` 的 `GraphQLView` 完全异步化。
只需在 `urls.py` 中引用此类即可享受异步解析带来的性能优势。

```python
from async_graphql_view import AsyncGraphQLView

urlpatterns = [
    path("graphql/", AsyncGraphQLView.as_view(graphiql=True)),
]
```
