# Generated by Django 4.2.1 on 2023-05-31 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='project')),
                ('projectName', models.CharField(default='', max_length=50)),
                ('info', models.CharField(default='', max_length=50)),
                ('Link', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
