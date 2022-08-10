from multiprocessing.pool import IMapUnorderedIterator
from typing import Optional

from pydantic import BaseModel, Field
# このバージョンだと上だけだとFiledが読み取れず、下の文でFiledが読み取れた
from pydantic.fields import Field

# class TaskBase(BaseModel):
#     title: Optional[str] = Field(None, example="クリーニングを取りに行く")


# class TaskCreate(TaskBase):
#     pass


# class TaskCreateResponse(TaskCreate):
#     id: int

#     class Config:
#         orm_mode = True


# class Task(TaskBase):
#     id: int
#     done: bool = Field(False, description="完了フラグ")

#     class Config:
#         orm_mode = True


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")

class TaskCreate(TaskBase):
    # title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    pass

class TaskCreateResponce(TaskCreate):
    id: int

    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    # title: Optional[str] = Field(None, example="クリーニングを取りに行く")
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True






