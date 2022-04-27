# Generated by Django 2.0.7 on 2022-04-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymApp', '0008_auto_20220427_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='membershipType',
        ),
        migrations.AddField(
            model_name='client',
            name='Client_role',
            field=models.CharField(choices=[('M', 'Manager'), ('C', 'Client')], default='C', max_length=1),
        ),
    ]