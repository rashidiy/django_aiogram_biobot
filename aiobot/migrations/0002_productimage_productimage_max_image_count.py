# Generated by Django 4.2.1 on 2023-05-21 08:28

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aiobot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images', validators=[django.core.validators.validate_image_file_extension])),
                ('order', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='aiobot.product')),
            ],
        ),
        migrations.AddConstraint(
            model_name='productimage',
            constraint=models.CheckConstraint(check=models.Q(('order__lte', 10)), name='max_image_count'),
        ),
    ]