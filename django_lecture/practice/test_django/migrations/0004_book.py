# Generated by Django 3.2.6 on 2021-08-26 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_django', '0003_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20, null=True)),
                ('price', models.IntegerField(default=0)),
                ('published_date', models.DateField(null=True)),
            ],
        ),
    ]