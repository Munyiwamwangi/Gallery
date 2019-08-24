# Generated by Django 2.2.4 on 2019-08-24 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel', models.CharField(max_length=50)),
                ('food', models.CharField(max_length=50)),
                ('epic', models.CharField(max_length=50)),
                ('landscape', models.CharField(max_length=50)),
                ('portrait', models.CharField(max_length=50)),
                ('heritage', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='articles/')),
                ('image_name', models.CharField(max_length=50)),
                ('descritption', models.TextField()),
                ('url', models.CharField(max_length=2000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Editor')),
            ],
        ),
    ]
