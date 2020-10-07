from django.db import models
from django.contrib.auth.models import User
# db / hyosun / 1212
# 지점명 / 픽업시간 / 상품목록 / 픽업 준비 상황 / 글쓴이 (기본생성)
class DriveThru(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    shop = models.CharField(max_length=20) # 지점명 (지점선택에서 받아오기,  직접 여기서 입력 x)
    items = models.TextField() # 상품목록 (장바구니에서 받아오기, 직접 여기서 입력 x)
    state = models.IntegerField(default=0) # 픽업 준비 상황 (신청완료 = 0 (디폴트) / 상품준비중 = 1 / 준비완료, 픽업대기 = 2 / 픽업완료 = 3)
    pick_date = models.DateTimeField() # 픽업날짜 (사용자가 선택)
    pub_date = models.DateTimeField(auto_now=True) # 작성시간 (자동기입)