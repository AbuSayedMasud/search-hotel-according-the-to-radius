from django.contrib.gis.db import models
from django.utils.text import slugify
# from django.db import models​
from django.contrib.gis.geos import Point,Polygon



# Create your models here.


# class hotels(models.Model):
#     hotel_name=models.CharField(max_length=100)
#     Address=models.TextField()
#     Description=models.TextField()
#     Geopoint = models.PointField()
#     Lat=models.FloatField()
#     Lon=models.FloatField() 
class hotels_Details(models.Model):
    hotel_name=models.CharField(max_length=100)
    Address=models.TextField()
    Description=models.TextField()
    
    Image_field=models.ImageField(upload_to="static", default="upload")
    Geopoint = models.PointField()
    Latitude =models.FloatField()
    Longitude=models.FloatField()  
    # Polygon_Field=models.PolygonField(srid=4326,null=True,blank=True)
    # My_bbox_polygon=models.PolygonField(srid=4326,null=True,blank=True)
    def save(self, *args, **kwargs):
        self.Geopoint= Point(self.Longitude,self.Latitude)
        
        print(self.Geopoint)
        
        super(hotels_Details, self).save(*args, **kwargs)

