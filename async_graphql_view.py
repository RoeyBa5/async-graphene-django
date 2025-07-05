"""Async wrapper for graphene-django's GraphQLView."""

from typing import Optional

from graphene_django.views import GraphQLView
from graphql import ExecutionResult


class AsyncGraphQLView(GraphQLView):
    """GraphQLView with asynchronous execution of queries."""

    async def execute_graphql_request(
        self,
        request,
        data,
        query: str,
        variables: Optional[dict] = None,
        operation_name: Optional[str] = None,
        show_graphiql: bool = False,
    ) -> Optional[ExecutionResult]:
        if not query:
            return None

        context = self.get_context(request)
        middleware = self.get_middleware(request)

        return await self.schema.execute_async(
            query,
            variables=variables,
            operation_name=operation_name,
            context_value=context,
            middleware=middleware,
            root_value=self.get_root_value(request),
        )
