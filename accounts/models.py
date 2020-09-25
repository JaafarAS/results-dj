from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    USER_TYPE=[
        ('المرحلة الاولى','المرحلة الاولى'),
        ('المرحلة الثانية','المرحلة الثانية'),
        ('المرحلة الثالثة','المرحلة الثالثة'),
        ('المرحلة الرابعة', 'المرحلة الرابعة'),
    ] 
    user_type = models.CharField(max_length=30, choices=USER_TYPE , null=True , default= '' ,blank= True)


    
    EVALUATE=[
        ('امتياز', 'امتياز'),
        ('جيد جداً', 'جيد جداً'),
        ('جيد', 'جيد'),
        ('متوسط', 'متوسط'),
        ('مقبول', 'مقبول'),
        ('ضعيف', 'ضعيف'),
    ]

    computer_programming = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    electric_workshop = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    electrical_eng = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    mathematics = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    digital_logic = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    human_rights = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    physics = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    computer_principles = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)

    result_1 = models.CharField(max_length=30, null=True , default= '' ,blank= True)
    download_1 = models.CharField(max_length=30,  null=True , default= '' ,blank= True)
    notice_1 = models.CharField(max_length=30,  null=True , default= '' ,blank= True)
    

    technical_microprocessors = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    operating_system = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    digital_system = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    electronice_eng = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    data_structure = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    object_oriened_programming = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    eng_mathematics = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    training_2 = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)


    result_2 = models.CharField(max_length=30, null=True , default= '' ,blank= True)
    download_2 = models.CharField(max_length=30,  null=True , default= '' ,blank= True)
    notice_2 = models.CharField(max_length=30,  null=True , default= '' ,blank= True)
    


    communication = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    software_eng = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    digital_signal_processing = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    java = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    database = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    adv_eng_mathematics = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    computer_architecture = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    training_3 = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)


    result_3 = models.CharField(max_length=30, null=True , default= '' ,blank= True)
    download_3 = models.CharField(max_length=30,  null=True , default= '' ,blank= True)
    notice_3 = models.CharField(max_length=30,  null=True , default= '' ,blank= True)
    



    computer_and_data_security = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    computer_control = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    computer_networks = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    digital_image_processing = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    computer_interface = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    real_time_systems = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)
    advance_software_eng = models.CharField(max_length=30, choices=EVALUATE , null=True , default= '' ,blank= True)

    result_4 = models.CharField(max_length=30, null=True , default= '' ,blank= True)
    download_4 = models.CharField(max_length=30,  null=True , default= '' ,blank= True)
    notice_4 = models.CharField(max_length=30,  null=True , default= '' ,blank= True)
    
  

    def __str__(self):
        return str(self.user.first_name)

@receiver(post_save , sender=User)
def create_profile(sender,instance , created , **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )
