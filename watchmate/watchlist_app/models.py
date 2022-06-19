from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=200)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.TextField(max_length=200)
    platform = models.ForeignKey(to=StreamingPlatform, on_delete=models.CASCADE, related_name='watchlist')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    watchlist = models.ForeignKey(to=WatchList, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.title

# class Movie(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(max_length=200)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name
