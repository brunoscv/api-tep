# Generated by Django 2.2.3 on 2019-07-15 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
    ]
