# Generated by Django 4.0.4 on 2022-05-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
