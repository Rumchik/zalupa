# Generated by Django 2.0.13 on 2019-09-18 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20190916_0333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ammo',
            name='ammo_slug',
        ),
        migrations.RemoveField(
            model_name='helmet',
            name='helmet_slug',
        ),
        migrations.RemoveField(
            model_name='mobility_limiting_means',
            name='mlm_slug',
        ),
        migrations.RemoveField(
            model_name='service_animals',
            name='sa_slug',
        ),
        migrations.RemoveField(
            model_name='special_gas_facilities',
            name='sgf_slug',
        ),
        migrations.RemoveField(
            model_name='special_sticks',
            name='ss_slug',
        ),
        migrations.RemoveField(
            model_name='stun_devices',
            name='sd_slug',
        ),
        migrations.RemoveField(
            model_name='vest',
            name='vest_slug',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='weapon_slug',
        ),
    ]
