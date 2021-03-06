# Generated by Django 3.2.12 on 2022-03-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_keyboard_keycap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keycap',
            name='material',
            field=models.CharField(choices=[('ABS', 'ABS'), ('PTB', 'ABS'), ('GMK', 'GMK')], default='ABS', max_length=5),
        ),
        migrations.AlterField(
            model_name='keycap',
            name='profile',
            field=models.CharField(choices=[('DSA', 'DSA'), ('SA', 'DSA'), ('CHERRY', 'Cherry'), ('XDA', 'XDA')], default='DSA', max_length=6),
        ),
    ]
