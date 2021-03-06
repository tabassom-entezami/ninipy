# Generated by Django 4.0.4 on 2022-05-01 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='subs',
            field=models.ManyToManyField(related_name='subs_category', to='Product.subcategory'),
        ),
    ]
