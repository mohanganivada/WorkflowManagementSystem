# Generated by Django 4.0.8 on 2023-02-02 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cview', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tblcviewsubservices',
            name='cv_service',
        ),
        migrations.RemoveField(
            model_name='tbluseractivities',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tblusereducation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tbluserexperience',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tblusermaster',
            name='user_role',
        ),
        migrations.RemoveField(
            model_name='tbluserprof',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tbluserprojects',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usertechskills',
            name='user',
        ),
        migrations.DeleteModel(
            name='CviewServicesMaster',
        ),
        migrations.DeleteModel(
            name='TblCviewSubServices',
        ),
        migrations.DeleteModel(
            name='TblRoleMaster',
        ),
        migrations.DeleteModel(
            name='TblUserActivities',
        ),
        migrations.DeleteModel(
            name='TblUserEducation',
        ),
        migrations.DeleteModel(
            name='TblUserExperience',
        ),
        migrations.DeleteModel(
            name='TblUserMaster',
        ),
        migrations.DeleteModel(
            name='TblUserProf',
        ),
        migrations.DeleteModel(
            name='TblUserProjects',
        ),
        migrations.DeleteModel(
            name='UserTechSkills',
        ),
    ]
