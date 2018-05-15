# Generated by Django 2.0.5 on 2018-05-12 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_de_capa', models.ImageField(blank=True, null=True, upload_to='capa')),
                ('nome', models.CharField(max_length=35)),
                ('discricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('discricao', models.TextField()),
                ('local', models.CharField(blank=True, max_length=100, null=True)),
                ('dataInicio', models.DateTimeField(null=True, verbose_name='Data e Hora de Inicio')),
                ('dataFim', models.DateTimeField(null=True, verbose_name='Data e Hora do terminio')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='compromissoFoto')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=45)),
                ('bio', models.TextField()),
                ('telefone', models.CharField(max_length=12, null=True)),
                ('foto_de_Perfil', models.ImageField(blank=True, null=True, upload_to='perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nometarefa', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AgendaInstitucional',
            fields=[
                ('agenda_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Agenda.Agenda')),
            ],
            bases=('Agenda.agenda',),
        ),
        migrations.CreateModel(
            name='AgendaPrivada',
            fields=[
                ('agenda_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Agenda.Agenda')),
            ],
            bases=('Agenda.agenda',),
        ),
        migrations.CreateModel(
            name='AgendaPublica',
            fields=[
                ('agenda_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Agenda.Agenda')),
            ],
            bases=('Agenda.agenda',),
        ),
        migrations.CreateModel(
            name='CompromissoInstitucional',
            fields=[
                ('compromisso_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Agenda.Compromisso')),
                ('compromisso', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='Agenda.Tarefas')),
            ],
            bases=('Agenda.compromisso',),
        ),
        migrations.CreateModel(
            name='CompromissoPessoal',
            fields=[
                ('compromisso_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Agenda.Compromisso')),
                ('compromisso', models.CharField(choices=[('aniversario', 'Aniversário'), ('evento', 'Evento'), ('lembrete', 'Lembrete'), ('meta', 'Meta'), ('outro', 'Outro')], max_length=20)),
            ],
            bases=('Agenda.compromisso',),
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Agenda.Pessoa')),
                ('endereco', models.CharField(max_length=255, null=True)),
            ],
            bases=('Agenda.pessoa',),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='usuario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agendapublica',
            name='compromissoPessoal',
            field=models.ManyToManyField(blank=True, to='Agenda.CompromissoPessoal'),
        ),
        migrations.AddField(
            model_name='agendapublica',
            name='dono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agenda.Pessoa'),
        ),
        migrations.AddField(
            model_name='agendapublica',
            name='seguem',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agendaprivada',
            name='compromissoPessoal',
            field=models.ManyToManyField(blank=True, to='Agenda.CompromissoPessoal'),
        ),
        migrations.AddField(
            model_name='agendaprivada',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agenda.Pessoa'),
        ),
        migrations.AddField(
            model_name='agendainstitucional',
            name='compromissoInstitucional',
            field=models.ManyToManyField(blank=True, to='Agenda.CompromissoInstitucional'),
        ),
        migrations.AddField(
            model_name='agendainstitucional',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agenda.Instituicao'),
        ),
        migrations.AddField(
            model_name='agendainstitucional',
            name='seguem',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
