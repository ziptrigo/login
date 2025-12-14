from django.db import models


class UserServicePermission(models.Model):
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='service_permissions',
    )
    service = models.ForeignKey(
        'service.Service',
        on_delete=models.CASCADE,
        related_name='user_permissions',
    )
    permission = models.ForeignKey(
        'permission.Permission',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('user', 'service', 'permission')
