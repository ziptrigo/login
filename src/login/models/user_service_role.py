from django.db import models


class UserServiceRole(models.Model):
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='service_roles',
    )
    service = models.ForeignKey(
        'service.Service',
        on_delete=models.CASCADE,
        related_name='user_roles',
    )
    role = models.ForeignKey(
        'role.Role',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('user', 'service', 'role')
