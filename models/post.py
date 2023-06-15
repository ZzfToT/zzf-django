from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=64, db_index=True)
    create_date = models.DateTimeField("date created")
    categories = models.JSONField(null=True);
    tags = models.JSONField(null=True);
    mdfile = models.FilePathField(path="/home/zzf/markdown", match=".*\.md$");

    def __str__(self):
        return self.title

