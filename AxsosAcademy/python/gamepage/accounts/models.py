from django.contrib.auth.models import AbstractUser
from django.db import models

GENRE_CHOICES = [
    ('ACTION', 'Action'),
    ('RPG', 'RPG'),
    ('ARCADE', 'Arcade'),
    ('STRATEGY', 'Strategy'),
    ('TACTICAL', 'Tactical Shooter'),
    ('ADVENTURE', 'Adventure'),
]

RATE_CHOICES = [(i, str(i)) for i in range(1, 6)]


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    avatar_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.get_full_name() or self.username


class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    release_date = models.DateField()
    description = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='games')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='ratings')
    rate = models.IntegerField(choices=RATE_CHOICES)

    class Meta:
        unique_together = ('user', 'game')


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorites')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='favorited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')