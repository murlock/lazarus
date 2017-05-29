from django.db import models
from django.forms import ModelForm

# Create your models here.
class TestSuite(models.Model):
    result = models.FileField(upload_to="archive/%Y%m%d/", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # FIXME: each build shoud contains:
    # - branch
    # - is_pr
    # - commit
    # FIXME later:
    # each build should contains number of (ok, failed, ..) results per test suite
    # it will help to detect regression between two runs


    def __unicode__(self):
        return "{o.pk} at {o.created_at}".format(o=self)


class TestSuiteForm(ModelForm):
    class Meta:
        model = TestSuite
        fields = [ 'result' ]
