from sqlmodel import Field, SQLModel

class tasks(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    done: bool | None = Field(default=None, index=True)