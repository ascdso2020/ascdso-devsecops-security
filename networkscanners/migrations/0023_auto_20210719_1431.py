# Generated by Django 3.1.12 on 2021-07-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("networkscanners", "0022_auto_20210705_1243"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskScheduleDb",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("task_id", models.TextField(blank=True, null=True)),
                ("target", models.TextField(blank=True, null=True)),
                ("schedule_time", models.TextField(blank=True, null=True)),
                ("project_id", models.TextField(blank=True, null=True)),
                ("scanner", models.TextField(blank=True, null=True)),
                ("periodic_task", models.TextField(blank=True, null=True)),
                ("updated_time", models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Task Schedule Data",
                "db_table": "taskscheduledb",
            },
        ),
        migrations.DeleteModel(
            name="task_schedule_db",
        ),
        migrations.AlterModelOptions(
            name="networkscandb",
            options={"verbose_name_plural": "Network Scans List"},
        ),
        migrations.AlterModelOptions(
            name="networkscanresultsdb",
            options={"verbose_name_plural": "Network Scans Data"},
        ),
        migrations.RemoveField(
            model_name="networkscandb",
            name="project_id",
        ),
        migrations.RemoveField(
            model_name="networkscandb",
            name="username",
        ),
        migrations.RemoveField(
            model_name="networkscanresultsdb",
            name="project_id",
        ),
        migrations.RemoveField(
            model_name="networkscanresultsdb",
            name="username",
        ),
    ]