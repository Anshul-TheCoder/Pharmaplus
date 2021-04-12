# Generated by Django 2.2.7 on 2019-11-12 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmaplus', '0003_auto_20191111_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='stores',
            name='city',
            field=models.ForeignKey(help_text='City', on_delete=django.db.models.deletion.CASCADE, to='pharmaplus.City'),
        ),
    ]
