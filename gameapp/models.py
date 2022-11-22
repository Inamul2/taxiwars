from django.db import models

class GameData(models.Model):
    ID = models.AutoField(primary_key=True)
    value = models.CharField(max_length=6)

    def __str__(self):
        return f"Game{self.ID}"