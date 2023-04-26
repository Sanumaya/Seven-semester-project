# Generated by Django 3.2.4 on 2022-04-20 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.CharField(max_length=15)),
                ('glucose', models.CharField(max_length=15)),
                ('blood_pressure', models.CharField(max_length=15)),
                ('skin_thickness', models.CharField(max_length=15)),
                ('insulin', models.CharField(max_length=15)),
                ('bmi', models.CharField(max_length=15)),
                ('diabetes_predigree_function', models.CharField(max_length=15)),
                ('age', models.CharField(max_length=15)),
                ('owner', models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
