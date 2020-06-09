from django.db import models
from django.utils import timezone
# 所有以 from 或 import 开始的所有行，都是需要从其他文件中添加一些内容。 所以与其复制和粘贴同样的内容，我们可以用 from...... import......来导入这些文件.


class Post(models.Model):
    # class Post(models.Model): - 这行是用来定义我们的模型 (这是一个 对象)
    # models.Model 表明Post是一个Django模型，所以Django知道它应该被保存在数据库中
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
