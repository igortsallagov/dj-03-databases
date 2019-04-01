# Generated by Django 2.1.1 on 2019-03-29 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('display', models.FloatField(max_length=5, verbose_name='Диагональ экрана')),
                ('resolution', models.CharField(max_length=20, verbose_name='Разрешение экрана')),
                ('camera', models.CharField(max_length=50, verbose_name='Камера (Мп)')),
                ('memory', models.PositiveIntegerField(max_length=10, verbose_name='Память (Гб)')),
                ('phone_os', models.CharField(max_length=20, verbose_name='Операционная система')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('phone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='phones.Phone')),
                ('lightning', models.BooleanField(verbose_name='Разъем Lightning')),
            ],
            bases=('phones.phone',),
        ),
        migrations.CreateModel(
            name='Samsung',
            fields=[
                ('phone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='phones.Phone')),
                ('extra_memory', models.PositiveIntegerField(max_length=10, verbose_name='Карта памяти (Гб)')),
            ],
            bases=('phones.phone',),
        ),
    ]
