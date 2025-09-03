from django.core.management.base import BaseCommand
from apps.main.models import SampleTimestamp


class Command(BaseCommand):
    help = "チェック: DateTimeFieldのtzinfoとstrftimeの挙動"

    def handle(self, *args, **options):
        self.stdout.write("\n=== 新規作成時 ===")
        obj = SampleTimestamp.objects.create(name="test")

        self._dump_datetime("生成直後", obj.created_at)

        self.stdout.write("\n=== DBから再取得後 ===")
        obj = SampleTimestamp.objects.get(id=obj.id)
        self._dump_datetime("DB取得後", obj.created_at)

    def _dump_datetime(self, label, dt):
        from django.utils.timezone import localtime

        self.stdout.write(f"{label}: {dt} (tzinfo={dt.tzinfo})")
        self.stdout.write(f"  strftime: {dt.strftime('%Y-%m-%d %H:%M:%S')}")

        try:
            local = localtime(dt)
            self.stdout.write(f"  localtime + strftime: {local.strftime('%Y-%m-%d %H:%M:%S %Z')}")
        except Exception as e:
            self.stdout.write(f"  localtime failed: {e}")
