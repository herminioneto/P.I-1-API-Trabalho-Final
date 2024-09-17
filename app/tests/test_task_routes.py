from fastapi import status

from app import models


def test_task_count(client, db):
    task_count = db.query(models.Task).count()

    response = client.get("api/tasks")

    assert response.status_code == status.HTTP_200_OK

    tasks = response.json()

    assert len(tasks) == task_count
