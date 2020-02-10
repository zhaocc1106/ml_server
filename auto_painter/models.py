from django.db import models


# Create your models here.
class AutoPainter(models.Model):
    class_name = models.CharField(max_length=100)
    begin_stroke = models.CharField(max_length=4096)
    follow_stroke = models.CharField(max_length=4096)

    def __str__(self):
        return "class_name: {0}, begin_stroke: {1}, follow_stroke: {2}" \
            .format(self.class_name, self.begin_stroke,
                    self.follow_stroke)
