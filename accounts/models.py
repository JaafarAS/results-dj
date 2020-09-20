from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    USER_TYPE=[
        ('first','المرحلة الاولى'),
        ('second','المرحلة الثانية '),
        ('third','المرحلة الثالثة'),
        ('fourth', 'المرحلة الرابعة'),
    ] 
    user_type = models.CharField(max_length=30, choices=USER_TYPE , null=True , blank= True)


    
    EVALUATE=[
        ('franchise', 'امتياز'),
        ('very_good', 'جيد جداً'),
        ('good', 'جيد'),
        ('average', 'متوسط'),
        ('passable', 'مقبول'),
        ('weak', 'ضعيف'),
    ]

    computer_programming = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    electric_workshop = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    electrical_eng = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    mathematics = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    digital_logic = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    human_rights = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    pysics = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    computer_principles = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    

    technical_microprocessors = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    operating_system = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    digital_system = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    electronice_eng = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    data_structure = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    object_oriened_programming = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    eng_mathematics = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    training_2 = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)



    communication = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    software_eng = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    digital_signal_processing = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    java = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    database = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    adv_eng_mathematics = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    computer_architecture = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    training_3 = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)



    computer_and_data_security = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    computer_control = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    computer_networks = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    digital_image_processing = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    computer_interface = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    real_time_systems = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
    advance_software_eng = models.CharField(max_length=30, choices=EVALUATE , null=True , blank= True)
  

    def __str__(self):
        return str(self.user)

@receiver(post_save , sender=User)
def create_profile(sender,instance , created , **kwargs):
    if created:
        profile.objects.create(
            user = instance
        )
