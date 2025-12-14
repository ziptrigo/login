from django.db import models


class UserGlobalPermission(models.Model):
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='global_permissions',
    )
    permission = models.ForeignKey(
        'permission.Permission',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('user', 'permission')
