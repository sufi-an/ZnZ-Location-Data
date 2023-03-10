from multiprocessing import Condition
from venv import create
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.deletion import SET_NULL
from authentication.models import User


APP_TYPE = (
    ('M', 'Mobile'),
    ('W', 'Web'),
)

STATUS_CHOICES = (
    ('D', 'Draft'),
    ('P', 'Published'),
)


class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Division(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)

class District(models.Model):
    division_id = models.ForeignKey(
        Division, on_delete=CASCADE, null=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)


class Thana(models.Model):
    division_id = models.ForeignKey(
        Division, on_delete=CASCADE, null=True)
    district_id = models.ForeignKey(
        District, on_delete=CASCADE, null=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)


class Union(models.Model):
    division_id = models.ForeignKey(
        Division, on_delete=CASCADE, null=True)
    district_id = models.ForeignKey(
        District, on_delete=CASCADE, null=True)
    Thana_id = models.ForeignKey(
        Thana, on_delete=CASCADE, null=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)


class LocationPicture(models.Model):
    picture = models.ImageField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Location(models.Model):
    locationPicture = models.ForeignKey(
        LocationPicture, on_delete=SET_NULL, null=True,blank=True)
    division_id = models.ForeignKey(
        Division, on_delete=CASCADE, null=True)
    user = models.ForeignKey(
        User, on_delete=SET_NULL, null=True
    )
    category_id = models.ForeignKey(
        Category, on_delete=CASCADE, null=True,blank=True
    )
    district_id = models.ForeignKey(
        District, on_delete=CASCADE, null=True
    )
    thana_id = models.ForeignKey(
        Thana, on_delete=CASCADE, null=True
    )
    union_id = models.ForeignKey(
        Union, on_delete=CASCADE, null=True,blank=True
    )
    name = models.CharField(max_length=150, null=True, blank=True)
    lat_long = models.CharField(max_length=250, null=True, blank=True)
    lat = models.CharField(max_length=250, null=True, blank=True)
    long = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    landmark = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    app_type = models.CharField(choices=APP_TYPE, max_length=1, default='M')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.id)

    # this is manual process to save, default union = NA
    def save(self, *args, **kwargs):
        if not self.union_id:
            self.union_id = Union.objects.get(id=4623)
        return super(Location, self).save(*args, **kwargs)


class route(models.Model):
    user = models.ForeignKey(
        User, on_delete=SET_NULL, null=True
    )
    lat = models.CharField(max_length=250, null=True, blank=True)
    long = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class locationAll(models.Model):
    locationPicture_id = models.CharField(max_length=150, null=True, blank=True)
    division_id_id = models.CharField(max_length=150, null=True, blank=True)
    user_id = models.CharField(max_length=150, null=True, blank=True)
    category_id_id = models.CharField(max_length=150, null=True, blank=True)
    district_id_id = models.CharField(max_length=150, null=True, blank=True)
    thana_id_id = models.CharField(max_length=150, null=True, blank=True)
    union_id_id = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    lat_long = models.CharField(max_length=250, null=True, blank=True)
    lat = models.CharField(max_length=250, null=True, blank=True)
    long = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    landmark = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    app_type = models.CharField(max_length=150, null=True, blank=True)
    district_name = models.CharField(max_length=150, null=True, blank=True)
    category_name = models.CharField(max_length=150, null=True, blank=True)
    division_name = models.CharField(max_length=150, null=True, blank=True)
    union_name = models.CharField(max_length=150, null=True, blank=True)
    thana_name = models.CharField(max_length=150, null=True, blank=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'location_all'


class AssignTask(models.Model):
    user = models.ForeignKey(
        User, on_delete=SET_NULL, null=True
    )
    task_start_date = models.DateField()
    task_end_date = models.DateField()
    task_assign = models.CharField(max_length=500, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.task_assign)
    