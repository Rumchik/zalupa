# Generated by Django 2.0.13 on 2019-06-25 09:35

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190623_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobility_limiting_means',
            name='handcuffs_descrioption',
        ),
        migrations.RemoveField(
            model_name='service_animals',
            name='using_for',
        ),
        migrations.AddField(
            model_name='ammo',
            name='ammo_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder),
        ),
        migrations.AddField(
            model_name='ammo',
            name='common_view_ammo',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder),
        ),
        migrations.AddField(
            model_name='ammo',
            name='common_view_bullet',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder),
        ),
        migrations.AddField(
            model_name='ammo',
            name='pack_common_view',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder),
        ),
        migrations.AddField(
            model_name='mobility_limiting_means',
            name='handcuffs_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mobility_limiting_means',
            name='handcuffs_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder),
        ),
        migrations.AddField(
            model_name='mobility_limiting_means',
            name='handcuffs_title',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='service_animals',
            name='animals_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='service_animals',
            name='purpose',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='special_gas_facilities',
            name='gase_greande_title',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='special_sticks',
            name='special_sticks_title',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='stun_devices',
            name='stun_gun_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='stun_devices',
            name='stun_gun_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder),
        ),
        migrations.AddField(
            model_name='stun_devices',
            name='stun_gun_title',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='helmet',
            name='helmet_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder),
        ),
        migrations.AlterField(
            model_name='helmet',
            name='helmet_protection_class',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='helmet',
            name='helmet_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='mobility_limiting_means',
            name='handcuffs_material',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='service_animals',
            name='animals_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder),
        ),
        migrations.AlterField(
            model_name='service_animals',
            name='jaws_strength',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='special_gas_facilities',
            name='gase_grenade_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder),
        ),
        migrations.AlterField(
            model_name='special_gas_facilities',
            name='temprature_range_of_application',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='special_sticks',
            name='manufacturing_material',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='special_sticks',
            name='stick_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='stun_gun_formfactor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='vest',
            name='protection_class',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='vest',
            name='vest_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder),
        ),
        migrations.AlterField(
            model_name='vest',
            name='vest_title',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
