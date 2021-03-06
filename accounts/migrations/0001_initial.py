# Generated by Django 3.1.1 on 2020-09-20 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_programming', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('electric_workshop', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('electrical_eng', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('mathematics', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('digital_logic', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('human_rights', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('pysics', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('computer_principles', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('technical_microprocessors', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('operating_system', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('digital_system', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('electronice_eng', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('data_structure', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('object_oriened_programming', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('eng_mathematics', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('training_2', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('communication', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('software_eng', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('digital_signal_processing', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('java', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('database', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('adv_eng_mathematics', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('computer_architecture', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('training_3', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('computer_and_data_security', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('computer_control', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('computer_networks', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('digital_image_processing', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('computer_interface', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('real_time_systems', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('advance_software_eng', models.CharField(blank=True, choices=[('franchise', 'امتياز'), ('very_good', 'جيد جداً'), ('good', 'جيد'), ('average', 'متوسط'), ('passable', 'مقبول'), ('weak', 'ضعيف')], max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
