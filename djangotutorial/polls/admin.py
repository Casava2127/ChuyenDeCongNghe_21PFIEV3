from django.contrib import admin
from .models import Choice, Question

# Dạng xếp chồng (cao, tốn chỗ)
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

# Dạng bảng (gọn hơn)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

    # Hiển thị các cột trên trang list
    list_display = ["question_text", "pub_date", "was_published_recently"]

    # Thanh lọc theo trường ngày giờ
    list_filter = ["pub_date"]

    # Ô tìm kiếm
    search_fields = ["question_text"]

    # (Tuỳ chọn thêm) phân trang ít hơn cho dễ xem
    # list_per_page = 25

    # (Tuỳ chọn thêm) phân cấp theo ngày
    # date_hierarchy = "pub_date"


admin.site.register(Question, QuestionAdmin)
