from os import O_ASYNC
from turtle import title
from urllib import response
# from fastapi import APIRouter
from typing import List

import api.schemas.task as task_schema

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import api.cruds.task as task_crud
from api.db import get_db

router = APIRouter()

# @router.get("/tasks")
# async def list_task():
#     pass
# @router.get("/tasks", response_model=List[task_schema.Task])
# async def list_task():
#     return [task_schema.Task(id=1, title="1つ目のTODOタスク")]
@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    # return [task_schema.Task(id=1, title="1つ目のTODOタスク")]
    return await task_crud.get_tasks_with_done(db)


# @router.post("/tasks")
# async def create_task():
#     pass
@router.post("/tasks", response_model=task_schema.TaskCreateResponce)
async def create_task(
    task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    return await task_crud.create_task(db, task_body)

@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponce)
async def update_task(
    task_id: int, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return await task_crud.update_task(db, task_body, original=task)

@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return await task_crud.delete_task(db, original=task)

#ここでdictインスタンスに対して先頭に**をつけることで、dictをキーワード引数として展開し、task_schema.TaskCreateResponseクラスのコンストラクタに対して
# dictのkey/valueを渡す。つまりこれはtask_schema.TaskCreateResponse

@router.post("/tasks", response_model=task_schema.TaskCreateResponce)
async def create_task(task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponce(id=1, **task_body.dict())
