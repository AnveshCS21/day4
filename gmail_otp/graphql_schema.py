import strawberry
from email_service import send_email

# ✅ REQUIRED Query type (can be empty)
@strawberry.type
class Query:
    hello: str = "GraphQL is working"

# ✅ Mutation
@strawberry.type
class Mutation:

    @strawberry.mutation
    def send_email(self, email: str) -> str:
        send_email(email)
        return "Email sent successfully"

# ✅ Schema MUST have query
schema = strawberry.Schema(query=Query, mutation=Mutation)
