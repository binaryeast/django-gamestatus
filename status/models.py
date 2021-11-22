from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# https://docs.djangoproject.com/en/3.2/ref/models/fields/


class Status(models.Model):
    """
    기본 상태창 모델.
    모델은 데이터베이스 테이블(=엑셀 시트) 하나
    """
    level = models.IntegerField() # 숫자 필드
    description = models.CharField(max_length=1000) # 천자 제한


class Skill(models.Model):
    """
    스킬 모델.
    """
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    # Status에 연결
    skill_name = models.CharField(max_length=255)
    skill_description = models.TextField() # 길이 제한 없음
