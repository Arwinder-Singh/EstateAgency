# Generated by Django 4.2.3 on 2023-07-16 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(upload_to='profile_pics')),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=12)),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('skype', models.URLField()),
                ('fb', models.URLField()),
                ('twitter', models.URLField()),
                ('insta', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenities_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('property_type', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=200)),
                ('area', models.FloatField()),
                ('beds', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('garage', models.IntegerField(default=0, null=True)),
                ('map_location', models.URLField()),
                ('floor_plans', models.ImageField(upload_to='floor_plans')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agentProperty', to='Main.agent')),
                ('amenities', models.ManyToManyField(to='Main.amenities')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.ImageField(upload_to='property')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propertyImages', to='Main.property')),
            ],
        ),
    ]