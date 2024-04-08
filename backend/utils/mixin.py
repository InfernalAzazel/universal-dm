from datetime import datetime
import mongoengine


class DBTimestampMixin:
    create_at = mongoengine.DateTimeField(default=datetime.utcnow)
    update_at = mongoengine.DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        # 确保TimestampMixin作为Document的Mixin使用
        if not hasattr(super(), 'save'):
            raise TypeError("TimestampMixin can only be used with mongoengine.Document subclasses")
        if not self.create_at:
            self.create_at = datetime.utcnow()
        self.update_at = datetime.utcnow()
        return super().save(*args, **kwargs)  # type: ignore
