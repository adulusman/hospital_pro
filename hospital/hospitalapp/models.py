from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Departments(models.Model):
    dep_name = models.CharField(max_length=250)
    dep_desc = models.TextField()

    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    doc_name = models.CharField(max_length=250)
    doc_spec = models.TextField()
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_img = models.ImageField(upload_to='doc_img')

    def __str__(self):
        return 'Dr ' + str(self.doc_name)


class District(models.Model):
    Dist_name = models.CharField(max_length=50)

    def __str__(self):
        return self.Dist_name


class SubBranches(models.Model):
    sub_name = models.CharField(max_length=250)
    Dist_name = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_name


class Booking(models.Model):
    p_name = models.CharField(max_length=250)
    dob = models.DateField()
    phn = models.CharField(max_length=12)
    email = models.EmailField()
    gend = (
        ('male', "MALE"),
        ('female', "FEMALE"),
        ('other', "OTHER"))
    gender = models.CharField(max_length=10, choices=gend, default='other')
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doctor = ChainedForeignKey(Doctors,
                               chained_field='department',
                               chained_model_field='dep_name',
                               show_all=False,
                               auto_choose=True
                               )
    blood = (
        ('a+', "A+"),
        ('b+', "B+"),
        ('a-', "A-"),
        ('b-', "B-"),
        ('ab-', "AB-"),
        ('ab+', "AB+"),
        ('o+', "O+"),
        ('o-', "O-"))
    blood_group = models.CharField(max_length=10, choices=blood, default='other')

    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    sub_branch = ChainedForeignKey(
        SubBranches,
        chained_field='district',
        chained_model_field='Dist_name',
        show_all=False,
        auto_choose=True
    )
    booking_date = models.DateField()
    booked_on = models.DateTimeField(auto_now=True)
