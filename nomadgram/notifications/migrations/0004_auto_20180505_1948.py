# Generated by Django 2.0.4 on 2018-05-05 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20180504_1805'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-created_at']},
        ),
    ]
