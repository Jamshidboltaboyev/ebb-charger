# Generated by Django 4.2 on 2023-11-11 11:33

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
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='%Y/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(max_length=13, verbose_name='Qabul qiluvchi')),
                ('message_id', models.CharField(blank=True, editable=False, max_length=20, null=True, unique=True, verbose_name='Broker SMS ID')),
                ('text', models.CharField(max_length=160, verbose_name='Matn')),
                ('code', models.CharField(max_length=20, null=True, verbose_name='Kod')),
                ('sent', models.BooleanField(default=False, verbose_name="Jo'natildi")),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")),
                ('sent_time', models.DateTimeField(blank=True, null=True, verbose_name="Jo'natilgan vaqti")),
                ('ip', models.CharField(blank=True, max_length=128, null=True, verbose_name='Foydalanuvchi IP manzili')),
            ],
            options={
                'verbose_name': 'SMS',
                'verbose_name_plural': 'SMSlar',
            },
        ),
        migrations.CreateModel(
            name='PermissionsMixin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='custom_user_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QrCodeScanerCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='Сканлаган QR кодлар сони')),
                ('iphone', models.IntegerField(blank=True, null=True, verbose_name='Iphone')),
                ('android', models.IntegerField(blank=True, null=True, verbose_name='Android')),
                ('last_scan', models.DateTimeField(auto_now_add=True, verbose_name='Сканлаган сана')),
            ],
            options={
                'verbose_name': 'QR кодлар сони',
                'verbose_name_plural': 'QR кодлар сони',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('permissionsmixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.permissionsmixin')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('father_name', models.CharField(blank=True, max_length=150, null=True)),
                ('user_type', models.SmallIntegerField(choices=[(1, 'client'), (2, 'operator'), (3, 'admin')], default=1)),
                ('full_name', models.CharField(blank=True, max_length=150, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('free_charging_time', models.IntegerField(blank=True, null=True)),
                ('free_charging_to_date', models.DateField(blank=True, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('amount', models.FloatField(default=0, verbose_name='shaxsiy hisob')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(null=True)),
                ('birth_date_editable', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted at')),
                ('avatar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_image', to='accounts.media', verbose_name='Rasm')),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.permissionsmixin', models.Model),
        ),
        migrations.CreateModel(
            name='UserGift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Актив'), ('used', 'Фойдаланган'), ('expired', 'Муддати ўтган')], default='active', max_length=10, verbose_name='Статус')),
                ('expired_date', models.DateTimeField(blank=True, null=True, verbose_name='Муддати')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='gifts', to='accounts.user', verbose_name='Фойдаланувчи')),
            ],
            options={
                'verbose_name': 'Фойдаланувчи совгаси',
                'verbose_name_plural': 'Фойдаланувчи совгалари',
            },
        ),
        migrations.CreateModel(
            name='DeletedAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Телефон рақами')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Исм')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('reason', models.CharField(blank=True, max_length=255, null=True, verbose_name='Сабаби')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
            options={
                'verbose_name': 'Deleted account',
                'verbose_name_plural': 'Deleted accounts',
            },
        ),
        migrations.CreateModel(
            name='UserLoginDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Қурилма номи')),
                ('imei_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='IMEI')),
                ('login_time', models.DateTimeField(blank=True, null=True, verbose_name='Тизимга кирган санаси')),
                ('logged_out', models.BooleanField(blank=True, default=False)),
                ('logout_time', models.DateTimeField(blank=True, null=True, verbose_name='Тизимдан чиқиш санаси')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='devices', to='accounts.user', verbose_name='Фойдаланувчи')),
            ],
            options={
                'verbose_name': 'Фойдаланувчи қурилмаси',
                'verbose_name_plural': 'Фойдаланувчи қурилмалари',
                'unique_together': {('user', 'imei_code')},
            },
        ),
    ]