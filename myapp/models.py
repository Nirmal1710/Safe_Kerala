from django.db import models

# Create your models here.
from django.db import models

class Criminal(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    photo1 = models.CharField(max_length=200, null=True, blank=True)
    photo2 = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    place = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    post = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    adarcard = models.CharField(max_length=20, null=True, blank=True)
    fingerprint = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'criminal'




class Login(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'login'


class Notification(models.Model):
    date = models.DateField(null=True, blank=True)
    notification = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        db_table = 'notification'


class PoliceStation(models.Model):
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)
    station_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    place = models.CharField(max_length=50, null=True, blank=True)
    post = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'police_station'


class User(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    photo = models.CharField(max_length=200, null=True, blank=True)
    place = models.CharField(max_length=50, null=True, blank=True)
    post = models.CharField(max_length=50, null=True, blank=True)
    district = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'user'

class Labour(models.Model):
    # labour_id = models.AutoField(primary_key=True)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    labourname = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    dob = models.CharField(max_length=20, null=True, blank=True)
    marital_status = models.CharField(max_length=50, null=True, blank=True)
    native_place = models.CharField(max_length=50, null=True, blank=True)
    native_city = models.CharField(max_length=50, null=True, blank=True)
    native_state = models.CharField(max_length=50, null=True, blank=True)
    native_pin = models.IntegerField(null=True, blank=True)
    photo = models.CharField(max_length=200, null=True, blank=True)
    current_place = models.CharField(max_length=50, null=True, blank=True)
    current_district = models.CharField(max_length=50, null=True, blank=True)
    identification_mark1 = models.CharField(max_length=50, null=True, blank=True)
    identification_mark2 = models.CharField(max_length=50, null=True, blank=True)
    adarcard = models.BigIntegerField(null=True, blank=True)
    fingerprint = models.CharField(max_length=200, null=True, blank=True)
    job_type = models.CharField(max_length=50, null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    idcard_no = models.CharField(max_length=20, default='0')

    class Meta:
        db_table = 'labour'


class Complaints(models.Model):
    # complaint_id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    complaint = models.CharField(max_length=500, null=True, blank=True)
    reply = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    USER = models.ForeignKey(Login, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'complaints'

class Feedback(models.Model):
    # feedback_id = models.AutoField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'feedback'


class Skill(models.Model):
    skill_type = models.CharField(max_length=50, null=True, blank=True)
    WORKER = models.ForeignKey(Labour, on_delete=models.CASCADE)

    class Meta:
        db_table = 'skill'


class Request(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    WORKER = models.ForeignKey(Labour, on_delete=models.CASCADE)
    work_type = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True,default="pending")
    work_status = models.CharField(max_length=50, null=True, blank=True,default="pending")
    class Meta:
        db_table = 'request'


class Payment(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    REQUEST = models.ForeignKey(Request, on_delete=models.CASCADE)
    payment = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = 'Payment'

        
class Payments(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    REQUEST = models.ForeignKey(Request, on_delete=models.CASCADE)
    payment = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = 'Payments'


class Review(models.Model):
    # review_id = models.AutoField(primary_key=True)
    rating = models.CharField(max_length=50, null=True, blank=True)
    review = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    WORKER = models.ForeignKey(Labour, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'review'



