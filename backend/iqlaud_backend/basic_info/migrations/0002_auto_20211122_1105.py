# Generated by Django 3.2.8 on 2021-11-22 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='portfolio_images/')),
            ],
        ),
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='ContactFormModel',
        ),
    ]