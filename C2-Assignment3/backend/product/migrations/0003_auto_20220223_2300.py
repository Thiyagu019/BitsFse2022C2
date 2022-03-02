# Generated by Django 3.2.12 on 2022-02-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_initialprodDatabase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proddatabase',
            old_name='prodId',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='proddatabase',
            name='expiryDate',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='proddatabase',
            name='prodName',
            field=models.CharField(max_length=240),
        ),
        migrations.AlterField(
            model_name='proddatabase',
            name='prodPrice',
            field=models.CharField(max_length=20),
        ),
    ]