# Generated by Django 4.0.4 on 2022-05-04 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pos_table',
            name='brand',
            field=models.CharField(choices=[('Brighto', 'Brighto'), ('Daimond', 'Daimond'), ('Nippon', 'Nippon')], max_length=100),
        ),
    ]
