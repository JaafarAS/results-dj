# Generated by Django 3.1.1 on 2020-09-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='download_1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='download_2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='download_3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='download_4',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='notice_1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='notice_2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='notice_3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='notice_4',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='result_1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='result_2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='result_3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='result_4',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='adv_eng_mathematics',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='advance_software_eng',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='communication',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='computer_and_data_security',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='computer_architecture',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='computer_control',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='computer_interface',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='computer_networks',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='computer_principles',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='computer_programming',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='data_structure',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='database',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='digital_image_processing',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='digital_logic',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='digital_signal_processing',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='digital_system',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='electric_workshop',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='electrical_eng',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='electronice_eng',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='eng_mathematics',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='human_rights',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='java',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mathematics',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='object_oriened_programming',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='operating_system',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pysics',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='real_time_systems',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='software_eng',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='technical_microprocessors',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='training_2',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='training_3',
            field=models.CharField(blank=True, choices=[('امتياز', 'امتياز'), ('جيد جداً', 'جيد جداً'), ('جيد', 'جيد'), ('متوسط', 'متوسط'), ('مقبول', 'مقبول'), ('ضعيف', 'ضعيف')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('المرحلة الاولى', 'المرحلة الاولى'), ('المرحلة الثانية', 'المرحلة الثانية'), ('المرحلة الثالثة', 'المرحلة الثالثة'), ('المرحلة الرابعة', 'المرحلة الرابعة')], max_length=30, null=True),
        ),
    ]
