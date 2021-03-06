# Generated by Django 2.0.13 on 2019-06-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190614_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='mobility_limiting_means',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handcuffs_descrioption', models.TextField()),
                ('handcuffs_material', models.CharField(max_length=200)),
                ('handcuffs_mass', models.PositiveIntegerField()),
                ('number_of_links', models.PositiveIntegerField()),
                ('equipment', models.TextField()),
                ('number_of_openings', models.CharField(max_length=160)),
                ('rings_diameter', models.PositiveIntegerField()),
                ('guarantee_period', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='special_gas_facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gase_grenade_description', models.CharField(max_length=80)),
                ('gase_grenade_mass', models.PositiveIntegerField()),
                ('gase_grenade_diameter', models.PositiveIntegerField()),
                ('gase_grenade_length', models.PositiveIntegerField()),
                ('voleme_of_aerosol_cloud', models.CharField(max_length=100)),
                ('temprature_range_of_application', models.CharField(max_length=100)),
                ('gase_grenade_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='special_sticks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturing_method', models.CharField(max_length=80)),
                ('manufacturing_material', models.CharField(max_length=80)),
                ('stick_diameter', models.PositiveIntegerField()),
                ('stick_mass', models.PositiveIntegerField()),
                ('stick_length', models.PositiveIntegerField()),
                ('stick_description', models.TextField()),
                ('stick_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='stun_devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stun_gun_formfactor', models.CharField(max_length=100)),
                ('operating_principle', models.CharField(max_length=100)),
                ('electrodes', models.CharField(max_length=200)),
                ('voltage', models.PositiveIntegerField()),
                ('efficiency', models.CharField(max_length=100)),
                ('stun_gun_mass', models.PositiveIntegerField()),
                ('stun_gun_length', models.PositiveIntegerField()),
                ('stun_gun_height', models.PositiveIntegerField()),
                ('stun_gun_width', models.PositiveIntegerField()),
                ('material', models.CharField(max_length=80)),
                ('power_methods', models.CharField(max_length=160)),
                ('charging', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='special_means',
        ),
    ]
