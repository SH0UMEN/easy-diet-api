# Generated by Django 4.0.5 on 2023-07-27 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
    ]