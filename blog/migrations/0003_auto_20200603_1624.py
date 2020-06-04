# Generated by Django 3.0.6 on 2020-06-03 10:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('blog', '0002_blog'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='BlogPage',
        ),
    ]