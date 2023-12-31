# Generated by Django 1.11.20 on 2019-05-30 21:13


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import simple_history.models
import uuid


class Migration(migrations.Migration):  # lint-amnesty, pylint: disable=missing-class-docstring

    dependencies = [
        ('student', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entitlements', '0010_backfill_refund_lock'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalCourseEntitlement',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),  # lint-amnesty, pylint: disable=line-too-long
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),  # lint-amnesty, pylint: disable=line-too-long
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('course_uuid', models.UUIDField(help_text='UUID for the Course, not the Course Run')),
                ('expired_at', models.DateTimeField(blank=True, help_text='The date that an entitlement expired, if NULL the entitlement has not expired.', null=True)),  # lint-amnesty, pylint: disable=line-too-long
                ('mode', models.CharField(help_text='The mode of the Course that will be applied on enroll.', max_length=100)),  # lint-amnesty, pylint: disable=line-too-long
                ('order_number', models.CharField(max_length=128, null=True)),
                ('refund_locked', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),  # lint-amnesty, pylint: disable=line-too-long
                ('_policy', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='entitlements.CourseEntitlementPolicy')),  # lint-amnesty, pylint: disable=line-too-long
                ('enrollment_course_run', models.ForeignKey(blank=True, db_constraint=False, help_text='The current Course enrollment for this entitlement. If NULL the Learner has not enrolled.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='student.CourseEnrollment')),  # lint-amnesty, pylint: disable=line-too-long
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),  # lint-amnesty, pylint: disable=line-too-long
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),  # lint-amnesty, pylint: disable=line-too-long
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical course entitlement',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
