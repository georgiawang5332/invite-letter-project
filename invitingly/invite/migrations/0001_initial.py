# Generated by Django 4.0 on 2023-08-21 13:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiveMoney',
            fields=[
                ('autonoGive', models.AutoField(primary_key=True, serialize=False, verbose_name='編號')),
                ('nameGive', models.CharField(blank=True, help_text='ex: 王小明', max_length=255, null=True, verbose_name='真實姓名')),
                ('phoneGive', phonenumber_field.modelfields.PhoneNumberField(default=None, help_text='ex: +886928420424', max_length=128, region=None, unique=True, verbose_name='電話')),
                ('addressGive', models.CharField(blank=True, help_text='ex: 台北市信義區松高路12號3樓 ', max_length=255, null=True, verbose_name='地址')),
                ('emailGive', models.EmailField(blank=True, help_text='ex: admin123@gmail.com', max_length=255, null=True, verbose_name='信箱')),
                ('status', models.BooleanField(default=True, verbose_name='狀態')),
            ],
            options={
                'verbose_name': '給禮金',
                'verbose_name_plural': '給禮金建立',
                'db_table': 'inv_givemoney',
                'ordering': ('-phoneGive',),
            },
        ),
        migrations.CreateModel(
            name='NotAttend',
            fields=[
                ('autonoNo', models.AutoField(primary_key=True, serialize=False, verbose_name='編號')),
                ('nameNo', models.CharField(blank=True, help_text='ex: 王小明', max_length=255, null=True, verbose_name='真實姓名')),
                ('emailNo', models.EmailField(blank=True, help_text='ex: admin123@gmail.com', max_length=255, null=True, verbose_name='信箱')),
                ('msgNo', models.CharField(blank=True, help_text='ex: 給新人一段祝福語 ', max_length=255, null=True, verbose_name='留言')),
                ('status', models.BooleanField(default=True, verbose_name='狀態')),
            ],
            options={
                'verbose_name': '拒絕參加留言板',
                'verbose_name_plural': '留言板 建立',
                'db_table': 'inv_notattend',
                'ordering': ('-emailNo',),
            },
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('autono', models.AutoField(primary_key=True, serialize=False, verbose_name='編號')),
                ('name', models.CharField(help_text='ex: 王小明', max_length=255, verbose_name='真實姓名')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default=None, help_text='ex: +886928420424', max_length=128, region=None, unique=True, verbose_name='電話')),
                ('address', models.CharField(blank=True, help_text='ex: 台北市信義區松高路12號3樓 ', max_length=255, null=True, verbose_name='地址')),
                ('email', models.EmailField(blank=True, help_text='ex: admin123@gmail.com', max_length=255, null=True, verbose_name='信箱')),
                ('know', models.CharField(choices=[('新郎', '新郎'), ('新娘', '新娘'), ('共同朋友', '共同友人')], help_text='勾選一個', max_length=4, verbose_name='認識新人哪位')),
                ('diet', models.CharField(choices=[('葷食', '葷食'), ('素食', '素食')], help_text='勾選一個 ', max_length=2, verbose_name='飲食偏好')),
                ('baby_seat', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], help_text='勾選一個 ', max_length=1, verbose_name='嬰兒座椅數量')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='建立時間')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新時間')),
                ('status', models.BooleanField(default=True, verbose_name='狀態')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name': '邀請函',
                'verbose_name_plural': '邀請函建立',
                'db_table': 'inv_invitation',
                'ordering': ('-created_at',),
            },
        ),
    ]
