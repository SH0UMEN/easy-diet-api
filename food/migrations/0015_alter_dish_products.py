# Generated by Django 4.0.5 on 2022-12-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0014_alter_dish_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, through='food.DishProduct', to='food.product'),
        ),
    ]
