# Generated by Django 3.2.10 on 2021-12-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiConnect', '0003_auto_20211219_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id_student',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
