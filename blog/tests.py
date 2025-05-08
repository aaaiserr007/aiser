from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import BlogPost, Comment
from django.contrib.auth.models import User

class BlogPostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        self.post = BlogPost.objects.create(title="Test Post", content="This is a test post.", author=self.user)

    def test_blog_post_creation(self):
        url = reverse('blogpost-list')
        data = {'title': 'New Post', 'content': 'Content of the new post.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 2)

    def test_blog_post_list(self):
        url = reverse('blogpost-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_blog_post_update_permission(self):
        url = reverse('blogpost-detail', args=[self.post.id])
        data = {'title': 'Updated Title', 'content': 'Updated Content'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')

    def test_blog_post_update_no_permission(self):
        other_user = User.objects.create_user(username="otheruser", password="password")
        self.client.login(username="otheruser", password="password")
        url = reverse('blogpost-detail', args=[self.post.id])
        data = {'title': 'Updated Title', 'content': 'Updated Content'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_blog_post_creation_invalid_data(self):
        url = reverse('blogpost-list')
        data = {'title': '', 'content': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_blog_post_deletion(self):
        url = reverse('blogpost-detail', args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BlogPost.objects.count(), 0)

    def test_blog_post_deletion_no_permission(self):
        other_user = User.objects.create_user(username="otheruser", password="password")
        self.client.login(username="otheruser", password="password")
        url = reverse('blogpost-detail', args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthorized_blog_post_creation(self):
        self.client.logout()
        url = reverse('blogpost-list')
        data = {'title': 'Unauthorized Post', 'content': 'Should not be created.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class CommentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        self.post = BlogPost.objects.create(title="Test Post", content="This is a test post.", author=self.user)
        self.comment = Comment.objects.create(post=self.post, author=self.user, content="This is a comment.")

    def test_comment_creation(self):
        url = reverse('comment-list', args=[self.post.id])
        data = {'content': 'This is a new comment.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_comment_list(self):
        url = reverse('comment-list', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_comment_update_permission(self):
        url = reverse('comment-detail', args=[self.comment.id])
        data = {'content': 'Updated Comment'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated Comment')

    def test_comment_update_no_permission(self):
        other_user = User.objects.create_user(username="otheruser", password="password")
        self.client.login(username="otheruser", password="password")
        url = reverse('comment-detail', args=[self.comment.id])
        data = {'content': 'Updated Comment'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_comment_creation_invalid_data(self):
        url = reverse('comment-list', args=[self.post.id])
        data = {'content': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_comment_deletion(self):
        url = reverse('comment-detail', args=[self.comment.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)

    def test_comment_deletion_no_permission(self):
        other_user = User.objects.create_user(username="otheruser", password="password")
        self.client.login(username="otheruser", password="password")
        url = reverse('comment-detail', args=[self.comment.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)