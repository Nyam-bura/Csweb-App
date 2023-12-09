from django.db import models
from django.utils.translation import gettext as _


class Message(models.Model):
    user_id = models.PositiveIntegerField(_('user_id'))
    timestamp = models.DateField(_("timestamp"), auto_now=False, auto_now_add=True,null=True)
    message_body = models.CharField(_("message_body"),null=True,max_length=150)
  