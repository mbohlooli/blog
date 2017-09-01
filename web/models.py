# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from froala_editor.fields import FroalaField

from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=255)
    post_body = FroalaField()
    # TODO change editor

    def __unicode__(self):
        return "{}".format(self.post_title)
