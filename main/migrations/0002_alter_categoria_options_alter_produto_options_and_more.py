# Generated by Django 4.1.6 on 2023-02-13 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ('nome',), 'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ('nome',)},
        ),
        migrations.AlterIndexTogether(
            name='produto',
            index_together={('id', 'slug')},
        ),
    ]
