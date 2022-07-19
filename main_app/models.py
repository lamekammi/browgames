from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

RATINGS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)

GENRES = (
    ('A', 'Action'),
    ('AV', 'Adventure'),
    ('C', 'Casual'),
    ('I', 'Indie'),
    ('MMO', 'Massively Multiplayer Online Game'),
    ('R', 'Racing'),
    ('S', 'Sports'),
    ('SM', 'Simulation'),
    ('RPG', 'Role Playing Game'),
    ('ST', 'Strategy'),
    ('F', 'Free To Play'),
    ('EA', 'Early Access'),
    ('H', 'Horror'),
    ('D', 'Dating'),
    ('P', 'Puzzle'),
    ('VN', 'Visual Novel'),
    ('HO', 'Hidden Object'),
    ('SB', 'Sandbox Games'),
    ('TPS', 'Third Person Shooter'),
    ('FPS', 'First Person Shooter'),
    ('FR', 'Farming'),
    ('OW', 'Open World'),
    ('SU', 'Survival'),
    ('RY', 'Rhythm'),
    ('BG', 'Boardgame'),
    ('CG', 'Cardgame'),
    ('PB', 'Party Based'),
    ('SF', 'Science Fiction'),
    ('CO', 'Cooperative')
)

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genres_detail', kwargs={'pk': self.id})

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    link = models.CharField(max_length=1000)
    creator = models.CharField(max_length=50)
    
    genres = models.ManyToManyField(Genre)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})

class Comment(models.Model):
    rating = models.IntegerField(
        choices=RATINGS,
        default=RATINGS[0][0])
    comment = models.TextField(max_length=1000)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
   

    def __str__(self):
        return f"Rating: {self.get_rating_display()} Comment: {self.comment}"

class Photo(models.Model):
    url = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for game_id: {self.game_id} @{self.url}"