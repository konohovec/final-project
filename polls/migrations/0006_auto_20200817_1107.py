# Generated by Django 3.1 on 2020-08-17 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200817_0925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionnaire',
            options={'verbose_name': 'Опрос', 'verbose_name_plural': 'Опросы'},
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='question',
        ),
        migrations.AlterField(
            model_name='question',
            name='img',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='QuestionInQuestionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='polls.question', verbose_name='Вопрос')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire', to='polls.questionnaire', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Вопрос в опросе',
                'verbose_name_plural': 'Вопросы в опросе',
            },
        ),
    ]
