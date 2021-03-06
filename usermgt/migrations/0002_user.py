# Generated by Django 2.2.2 on 2019-06-29 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermgt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.PositiveSmallIntegerField(choices=[(0, 'M'), (1, 'F'), (2, 'Other')])),
                ('photo', models.ImageField(default='notfound', upload_to='media/photo/%Y/%m/%d')),
                ('resume', models.FileField(default='notfound', upload_to='media/resume/%Y/%m/%d')),
            ],
        ),
    ]
