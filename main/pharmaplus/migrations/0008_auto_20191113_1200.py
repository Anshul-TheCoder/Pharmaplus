# Generated by Django 2.2.7 on 2019-11-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmaplus', '0007_auto_20191112_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stores',
            name='phone',
            field=models.CharField(help_text='phone number of the store', max_length=50, null=True),
        ),
    ]
