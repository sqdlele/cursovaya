# Generated by Django 5.1.5 on 2025-04-26 09:31

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('image', models.ImageField(upload_to='news/', verbose_name='Изображение')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название услуги')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ц��на')),
                ('category', models.CharField(choices=[('Диагностика', 'Диагностика'), ('Ремонт', 'Ремонт'), ('ТО', 'ТО')], max_length=50, verbose_name='Категория')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/', verbose_name='Изображение')),
                ('original_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Оригинальная цена')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ['category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('status', models.CharField(choices=[('pending', 'В ожидании'), ('confirmed', 'Подтверждено'), ('completed', 'Завершено'), ('cancelled', 'Отменено')], default='pending', max_length=20, verbose_name='Статус')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Примечания')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('service_type', models.ManyToManyField(to='app.servicetype', verbose_name='Типы услуг')),
            ],
            options={
                'verbose_name': 'Запись на приём',
                'verbose_name_plural': 'Записи на приём',
                'ordering': ['-date', '-time'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=18, null=True, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('role', models.CharField(choices=[('client', 'Клиент'), ('support', 'Поддержка')], default='client', max_length=20, verbose_name='Роль')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='app.appointment', verbose_name='Запись на приём')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ServiceSpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servicetype', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Связь услуги и акции',
                'verbose_name_plural': 'Связи услуг и акций',
            },
        ),
        migrations.CreateModel(
            name='ServiceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('status', models.CharField(choices=[('pending', 'В ожидании'), ('in_progress', 'В процессе'), ('completed', 'Завершено'), ('cancelled', 'Отменено')], default='pending', max_length=20, verbose_name='Статус')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('mileage_at_service', models.IntegerField(blank=True, null=True, verbose_name='Пробег')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servicetype', verbose_name='Тип услуги')),
            ],
            options={
                'verbose_name': 'Запись об обслуживании',
                'verbose_name_plural': 'Записи об обслуживании',
            },
        ),
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('image', models.ImageField(upload_to='offers/', verbose_name='Изображение')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания акции')),
                ('is_one_time', models.BooleanField(default=False, verbose_name='Одноразовое предложение')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('services', models.ManyToManyField(related_name='special_offers', through='app.ServiceSpecialOffer', to='app.servicetype', verbose_name='Связанные услуги')),
            ],
            options={
                'verbose_name': 'Спецпредложение',
                'verbose_name_plural': 'Спецпредложения',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='servicespecialoffer',
            name='special_offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.specialoffer', verbose_name='Акция'),
        ),
        migrations.AlterUniqueTogether(
            name='servicespecialoffer',
            unique_together={('service', 'special_offer')},
        ),
    ]
