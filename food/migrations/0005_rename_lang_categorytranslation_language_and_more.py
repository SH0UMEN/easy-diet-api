# Generated by Django 4.0.5 on 2022-06-18 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_rename_language_categorytranslation_lang_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorytranslation',
            old_name='lang',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='producttranslation',
            old_name='lang',
            new_name='language',
        ),
    ]