# Generated by Django 4.0.4 on 2022-05-01 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_subcategory_category_subs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subs',
            field=models.ManyToManyField(blank=True, null=True, related_name='subs_category', to='Product.subcategory'),
        ),
    ]