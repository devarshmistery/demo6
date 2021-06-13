from django.db import models

# Create your models here.

class HomePage(models.Model):
    uName = models.CharField(default = "",max_length=100)
    Email = models.EmailField(default = "",max_length=100)
    password= models.CharField(default = "", max_length=50)
    cpassword  = models.CharField(default="",max_length=500)
    phone = models.CharField(default="", max_length=10)
    def __str__(self):
        return self.uName

class Admin_reg(models.Model):
    aname = models.CharField(default = "",max_length=100)
    aEmail = models.EmailField(default = "",max_length=100)
    apassword= models.CharField(default = "", max_length=50)
    acpassword  = models.CharField(default="",max_length=50)
    aphone = models.CharField(default="", max_length=10)
    def __str__(self):
        return self.aname

class Notice_view(models.Model):
    NName= models.ForeignKey("Admin_reg", on_delete=models.CASCADE)
    Nphone = models.CharField(default="", max_length=10)
    Nemail = models.EmailField(default = "",max_length=100)
    Nsubject = models.CharField(default="",max_length=500)
    Nnotice = models.CharField(default="",max_length=1000)
    date = models.DateField(blank=True,null=True,auto_now=False)
    def __str__(self):
        return self.Nemail

class Profile_view(models.Model):
    PNAme= models.ForeignKey("Homepage", on_delete=models.CASCADE,default="")
    PName= models.ForeignKey("Admin_reg", on_delete=models.CASCADE)
    Pemail = models.EmailField(default = "",max_length=100)
    Pflattype = models.CharField(default="",max_length=20)
    Pflatno = models.CharField(default="",max_length=20)
    Pphoto = models.FileField(upload_to="Files_Data/",default="",max_length=200)
    def __str__(self):
        return self.Pemail

class Complaint_view(models.Model):
    CName= models.ForeignKey("Admin_reg", on_delete=models.CASCADE)
    Cphone = models.CharField(default="", max_length=10)
    Cemail = models.EmailField(default = "",max_length=100)
    Ccategory = models.CharField(default="",max_length=500)
    Ccategorytype = models.CharField(default="",max_length=500)
    Cmessage = models.CharField(default="",max_length=1000)
    def __str__(self):
        return self.Cemail
