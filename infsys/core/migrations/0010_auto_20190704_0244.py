# Generated by Django 2.0.13 on 2019-07-03 23:44

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190625_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ammo',
            options={'verbose_name': 'Патроны', 'verbose_name_plural': 'Патроны'},
        ),
        migrations.AlterModelOptions(
            name='helmet',
            options={'verbose_name': 'Шлемы', 'verbose_name_plural': 'Шлемы'},
        ),
        migrations.AlterModelOptions(
            name='mobility_limiting_means',
            options={'verbose_name': 'Средства ограничения подвижности', 'verbose_name_plural': 'Средства ограничения подвижности'},
        ),
        migrations.AlterModelOptions(
            name='service_animals',
            options={'verbose_name': 'Служебные животные', 'verbose_name_plural': 'Служебные животные'},
        ),
        migrations.AlterModelOptions(
            name='special_gas_facilities',
            options={'verbose_name': 'Специальные газовые средства', 'verbose_name_plural': 'Специальные газовые средства'},
        ),
        migrations.AlterModelOptions(
            name='special_sticks',
            options={'verbose_name': 'Палки специальные', 'verbose_name_plural': 'Палки специальные'},
        ),
        migrations.AlterModelOptions(
            name='stun_devices',
            options={'verbose_name': 'Электрошоковые устройства', 'verbose_name_plural': 'Электрошоковые устройства'},
        ),
        migrations.AlterModelOptions(
            name='vest',
            options={'verbose_name': 'Бронежилеты', 'verbose_name_plural': 'Бронежилеты'},
        ),
        migrations.AlterModelOptions(
            name='weapon',
            options={'verbose_name': 'Оружие', 'verbose_name_plural': 'Оружие'},
        ),
        migrations.AddField(
            model_name='ammo',
            name='ammo_mass',
            field=models.IntegerField(blank=True, default=1, verbose_name='Масса патрона'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weapon',
            name='slug',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='ammo_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='Изображение маркировочных обохнаений'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='ammo_length',
            field=models.IntegerField(verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='ammo_name',
            field=models.CharField(max_length=80, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='ammo_producer',
            field=models.CharField(max_length=100, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='bottom_diameter',
            field=models.IntegerField(verbose_name='Диаметр донного упора'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='bullet_length',
            field=models.IntegerField(verbose_name='Длина пули, мм'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='bullet_mass',
            field=models.IntegerField(verbose_name='Масса пули, г'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='bullet_type',
            field=models.CharField(max_length=80, verbose_name='Тип пули'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='capsule_material_color',
            field=models.CharField(max_length=80, verbose_name='Цвет материала'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='capsule_type',
            field=models.CharField(max_length=80, verbose_name='Тип капсуля'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='case_diameter_bottom',
            field=models.IntegerField(verbose_name='Диаметр корпуса у донного упора'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='common_view_ammo',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='Изображение общего вида патрона'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='common_view_bullet',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='общее изображение пули'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='diameter',
            field=models.IntegerField(verbose_name='Диаметр капсуля'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='diameter_case_slope',
            field=models.IntegerField(verbose_name='Диаметр корпуса у ската'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='diameter_dults',
            field=models.IntegerField(verbose_name='Диаметр дульца'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='diameter_head_part',
            field=models.IntegerField(verbose_name='Диаметр ведущей части, мм'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='flange_diameter',
            field=models.IntegerField(verbose_name='Диаметр фланца'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='form',
            field=models.TextField(verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='head_part_form',
            field=models.CharField(max_length=80, verbose_name='Длина головной части'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='ignition_type',
            field=models.CharField(max_length=160, verbose_name='Тип воспламенитиля'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='markings',
            field=models.TextField(verbose_name='Маркировочное обозначение (описание)'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='material_color',
            field=models.CharField(max_length=80, verbose_name='Цвет материала'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='mounting_method',
            field=models.CharField(max_length=160, verbose_name='Способ крепления пули с гильзой'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='pack_common_view',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='Изображение упаковки'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='powder_mass',
            field=models.IntegerField(verbose_name='Масса порохового (иного) заряда'),
        ),
        migrations.AlterField(
            model_name='ammo',
            name='shell_length',
            field=models.IntegerField(verbose_name='Длина гильзы'),
        ),
        migrations.AlterField(
            model_name='helmet',
            name='helmet_description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='helmet',
            name='helmet_hight',
            field=models.PositiveIntegerField(verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='helmet',
            name='helmet_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='helmet',
            name='helmet_mass',
            field=models.PositiveIntegerField(verbose_name='Массса'),
        ),
        migrations.AlterField(
            model_name='helmet',
            name='helmet_material',
            field=models.CharField(max_length=200, verbose_name='МАтериал'),
        ),
        migrations.AlterField(
            model_name='helmet',
            name='helmet_protection_class',
            field=models.CharField(blank=True, max_length=80, verbose_name='Класс защиты'),
        ),
        migrations.AlterField(
            model_name='helmet',
            name='helmet_size',
            field=models.CharField(max_length=100, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='helmet',
            name='helmet_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='helmet',
            name='helmet_total_protection_area',
            field=models.PositiveIntegerField(verbose_name='Площадь защиты'),
        ),
        migrations.AlterField(
            model_name='helmet',
            name='helmet_width',
            field=models.PositiveIntegerField(verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='mobility_limiting_means',
            name='equipment',
            field=models.TextField(verbose_name='Снаряжение'),
        ),
        migrations.AlterField(
            model_name='mobility_limiting_means',
            name='guarantee_period',
            field=models.PositiveIntegerField(verbose_name='Период гарантии'),
        ),
        migrations.AlterField(
            model_name='mobility_limiting_means',
            name='handcuffs_description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='mobility_limiting_means',
            name='handcuffs_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='mobility_limiting_means',
            name='handcuffs_mass',
            field=models.PositiveIntegerField(verbose_name='Масса'),
        ),
        migrations.AlterField(
            model_name='mobility_limiting_means',
            name='handcuffs_material',
            field=models.CharField(blank=True, max_length=200, verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='mobility_limiting_means',
            name='handcuffs_title',
            field=models.CharField(blank=True, max_length=80, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='mobility_limiting_means',
            name='number_of_links',
            field=models.PositiveIntegerField(verbose_name='Число колец'),
        ),
        migrations.AlterField(
            model_name='mobility_limiting_means',
            name='number_of_openings',
            field=models.CharField(max_length=160, verbose_name='Число открытий/закрытий'),
        ),
        migrations.AlterField(
            model_name='mobility_limiting_means',
            name='rings_diameter',
            field=models.PositiveIntegerField(verbose_name='диаметр колец'),
        ),
        migrations.AlterField(
            model_name='service_animals',
            name='animals_description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='service_animals',
            name='animals_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='service_animals',
            name='animals_type',
            field=models.IntegerField(choices=[(0, 'Собака'), (1, 'Лощадь')], default=0, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='service_animals',
            name='average_hight',
            field=models.PositiveIntegerField(verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='service_animals',
            name='average_lenght',
            field=models.PositiveIntegerField(blank=True, verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='service_animals',
            name='jaws_strength',
            field=models.PositiveIntegerField(blank=True, verbose_name='Сила челюсти'),
        ),
        migrations.AlterField(
            model_name='service_animals',
            name='kind',
            field=models.CharField(max_length=100, verbose_name='Порода'),
        ),
        migrations.AlterField(
            model_name='service_animals',
            name='purpose',
            field=models.CharField(blank=True, max_length=200, verbose_name='Предназначение'),
        ),
        migrations.AlterField(
            model_name='special_gas_facilities',
            name='gase_greande_title',
            field=models.CharField(blank=True, max_length=80, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='special_gas_facilities',
            name='gase_grenade_description',
            field=models.CharField(max_length=80, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='special_gas_facilities',
            name='gase_grenade_diameter',
            field=models.PositiveIntegerField(verbose_name='Диаметр'),
        ),
        migrations.AlterField(
            model_name='special_gas_facilities',
            name='gase_grenade_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='special_gas_facilities',
            name='gase_grenade_length',
            field=models.PositiveIntegerField(verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='special_gas_facilities',
            name='gase_grenade_mass',
            field=models.PositiveIntegerField(verbose_name='Масса'),
        ),
        migrations.AlterField(
            model_name='special_gas_facilities',
            name='temprature_range_of_application',
            field=models.CharField(blank=True, max_length=100, verbose_name='Температурная область примениея'),
        ),
        migrations.AlterField(
            model_name='special_gas_facilities',
            name='voleme_of_aerosol_cloud',
            field=models.CharField(max_length=100, verbose_name='Объём аэйрозольного облака'),
        ),
        migrations.AlterField(
            model_name='special_sticks',
            name='manufacturing_material',
            field=models.CharField(blank=True, max_length=80, verbose_name='Материал производства'),
        ),
        migrations.AlterField(
            model_name='special_sticks',
            name='manufacturing_method',
            field=models.CharField(max_length=80, verbose_name='Метод производства'),
        ),
        migrations.AlterField(
            model_name='special_sticks',
            name='special_sticks_title',
            field=models.CharField(blank=True, max_length=80, verbose_name='Навание'),
        ),
        migrations.AlterField(
            model_name='special_sticks',
            name='stick_description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='special_sticks',
            name='stick_diameter',
            field=models.PositiveIntegerField(verbose_name='Диаметр палки'),
        ),
        migrations.AlterField(
            model_name='special_sticks',
            name='stick_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='Изображенрие'),
        ),
        migrations.AlterField(
            model_name='special_sticks',
            name='stick_length',
            field=models.PositiveIntegerField(verbose_name='Длинна палки'),
        ),
        migrations.AlterField(
            model_name='special_sticks',
            name='stick_mass',
            field=models.PositiveIntegerField(verbose_name='Масса палки'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='charging',
            field=models.CharField(max_length=300, verbose_name='Заряд'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='efficiency',
            field=models.CharField(max_length=100, verbose_name='Эффективная дальность'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='electrodes',
            field=models.CharField(max_length=200, verbose_name='Электроды'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='material',
            field=models.CharField(max_length=80, verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='operating_principle',
            field=models.CharField(max_length=100, verbose_name='Принцип применения'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='power_methods',
            field=models.CharField(max_length=160, verbose_name='Метод воздействия'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='stun_gun_description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='stun_gun_formfactor',
            field=models.CharField(blank=True, max_length=100, verbose_name='Формфактор'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='stun_gun_height',
            field=models.PositiveIntegerField(verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='stun_gun_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='stun_gun_length',
            field=models.PositiveIntegerField(verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='stun_gun_mass',
            field=models.PositiveIntegerField(verbose_name='Масса'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='stun_gun_title',
            field=models.CharField(blank=True, max_length=80, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='stun_gun_width',
            field=models.PositiveIntegerField(verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='stun_devices',
            name='voltage',
            field=models.PositiveIntegerField(verbose_name='Напряжение'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='body_material',
            field=models.CharField(max_length=80, verbose_name='Материал основы'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='cloth',
            field=models.CharField(max_length=200, verbose_name='Вид ткани'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='material_of_armor_elements',
            field=models.CharField(max_length=200, verbose_name='Материал бронеэлемента'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='materials',
            field=models.CharField(max_length=200, verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='protection_area',
            field=models.PositiveIntegerField(verbose_name='Площадь защищённой поверхности'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='protection_class',
            field=models.CharField(blank=True, max_length=40, verbose_name='Класс защиты'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='total_protection_area',
            field=models.PositiveIntegerField(verbose_name='Общая площадь защиты'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='vest_description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='vest_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='vest_mass',
            field=models.CharField(max_length=20, verbose_name='Масса'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='vest_size',
            field=models.CharField(max_length=40, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='vest_title',
            field=models.CharField(blank=True, max_length=80, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='vests_color',
            field=models.CharField(max_length=100, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='vests_length',
            field=models.PositiveIntegerField(verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='vests_width',
            field=models.PositiveIntegerField(verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='vest',
            name='wearing_type',
            field=models.CharField(max_length=100, verbose_name='Тип ношения'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='angle_between_hook_reflector',
            field=models.PositiveIntegerField(verbose_name='Угол между зацепом выбрасывателя и отражателем'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='angle_rifling',
            field=models.PositiveIntegerField(verbose_name='Угол наклона нарезов'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='automation_principle',
            field=models.TextField(verbose_name='Принцип отражателя'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='barrel_length',
            field=models.PositiveIntegerField(verbose_name='Длина ствола'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='caliber',
            field=models.PositiveIntegerField(verbose_name='Калибр'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='chamber_length',
            field=models.PositiveIntegerField(verbose_name='Длина патронника'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='chamber_shape',
            field=models.PositiveIntegerField(verbose_name='Форма патронника'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='direction_rifling',
            field=models.TextField(verbose_name='Направление нарезов'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='disassembly_procedure',
            field=models.TextField(verbose_name='Порядок неполной сборки и разборки'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='features',
            field=models.TextField(verbose_name='Технические и иные особенности, характерные для этой модели'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='gas_outlet',
            field=models.TextField(verbose_name='Наличае газоотводного отверстия в канале ствола'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='height',
            field=models.PositiveIntegerField(verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='length',
            field=models.PositiveIntegerField(verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='liner_removal_mech',
            field=models.TextField(verbose_name='Механиз удаления гильзы'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='location_details',
            field=models.TextField(verbose_name='Расположение на деталях оружия'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='locking_mech',
            field=models.TextField(verbose_name='Механизм запирания ствола'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='magazine',
            field=models.TextField(verbose_name='Магазин'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='magazines_capacity',
            field=models.PositiveIntegerField(verbose_name='Ёмкость магазина, патронов'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='marking_designation_description',
            field=models.TextField(verbose_name='Маркировочные обозначения (описание)'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='marking_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='Изображение маркировочных значений'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='mass',
            field=models.PositiveIntegerField(verbose_name='Масса'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='method_manufacture_barrel',
            field=models.TextField(verbose_name='Способ изготовления ствола'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='number_rifling',
            field=models.PositiveIntegerField(verbose_name='Количество нарезов'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='producer',
            field=models.CharField(max_length=100, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='safety_catch',
            field=models.TextField(verbose_name='Предохранитель'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='sleeves_reflection',
            field=models.TextField(verbose_name='Отражение гильзы'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='strikers_diameter',
            field=models.PositiveIntegerField(verbose_name='Диаметр бойка, мм'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='trace_pattern_sleev',
            field=models.TextField(verbose_name='Схема следов на гильзе'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='trace_pattern_sleev_image',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='Изображение следообразующих деталей'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='trigger_mech',
            field=models.TextField(verbose_name='Ударно-спусковой механизм'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='used_ammo',
            field=models.TextField(verbose_name='Применяемый патрон'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='weapons_name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='weapons_photo',
            field=models.ImageField(blank=True, upload_to=core.models.image_folder, verbose_name='Изображение оружия'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='width',
            field=models.PositiveIntegerField(verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='width_fields_rifling',
            field=models.PositiveIntegerField(verbose_name='Ширина полей нарезов'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='width_hook_extractor',
            field=models.PositiveIntegerField(verbose_name='Ширина зацепа выбрасывателя'),
        ),
    ]
