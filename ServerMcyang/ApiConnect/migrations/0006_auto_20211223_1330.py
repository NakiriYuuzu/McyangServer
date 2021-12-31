# Generated by Django 3.2.10 on 2021-12-23 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiConnect', '0005_auto_20211221_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id_course',
            field=models.ManyToManyField(blank=None, to='ApiConnect.Course'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id_course',
            field=models.ManyToManyField(to='ApiConnect.Course', verbose_name=''),
        ),
    ]
