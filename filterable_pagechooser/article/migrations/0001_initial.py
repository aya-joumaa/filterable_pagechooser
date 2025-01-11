# Generated by Django 4.2.17 on 2025-01-11 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0026_delete_uploadedimage'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='Is Active?')),
                ('displayed_title', models.CharField(blank=True, default='', max_length=250, verbose_name='Displayed Title')),
                ('type', models.CharField(blank=True, choices=[('', ''), ('sport', 'Sport'), ('medical', 'Medical'), ('economics', 'Economics'), ('technology', 'Technology')], default='', max_length=250, verbose_name='Title')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('gallery_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
            bases=('wagtailcore.page',),
        ),
    ]
