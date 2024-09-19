from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Test Task", completed=False)

    def test_get_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        data = {"title": "New Task", "description": "Some description"}
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        data = {"title": "Updated Task", "completed": True}
        response = self.client.patch(f'/api/tasks/{self.task.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)