file requireent
ảnh chụp màn hình
review mã nguồn
env trogn gitignore

tôi có 2 nhánh, nhánh main và nh1, tôi muốn thực hiện các commit trên nhánh nh1 nên tôi muốn tìm cách sao chép các commit từ nhánh nh1 sang main để báo cáo định kì, và tiếp tục phát triển trên nh1

Báo cáo tuần 2 
Tạo app mới (blog)

Định nghĩa models

Migration → database

Thử query xuôi/ngược.


Microsoft Windows [Version 10.0.22631.5771]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorial>C:/Users/Admin/Desktop/Ky9/ChuyenDeCongNghe/djangotutorial/venv/Scripts/activate.bat

(venv) C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorialpython manage.py startapp blog

(venv) C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorial>
(venv) C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorial>python manage.py makemigrations blog
Migrations for 'blog':
  blog\migrations\0001_initial.py
    + Create model Post
    + Create model Comment

(venv) C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorial>
(venv) C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorial>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, debug_toolbar, polls, sessions
Running migrations:
  Applying blog.0001_initial... OK
  Applying debug_toolbar.0001_initial... OK

(venv) C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorial>python manage.py shell
11 objects imported automatically (use -v 2 for details).

Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Post, Comment
>>> from datetime import date
>>>
>>> p1 = Post.objects.create(title="Bài đầu tiên", content="Hello Django!", published_date=date.today())
>>> Comment.objects.create(post=p1, author="Nam", message="Hay quá!")
<Comment: Comment by Nam>
>>> Comment.objects.create(post=p1, author="Lan", message="Cảm ơn đã chia sẻ")     
<Comment: Comment by Lan>
>>>
>>> # Truy vấn xuôi
>>> p1.comments.all()   # Lấy tất cả comment của post
<QuerySet [<Comment: Comment by Nam>, <Comment: Comment by Lan>]>
>>>
>>> # Truy vấn ngược
>>> c1 = Comment.objects.first()
>>> c1.post.title       # "Bài đầu tiên"
'Bài đầu tiên'
>>>

tiếp tục
tạo lại Blog và thực hiện 
tạo model đơn giản - query relation 
quêy phức tạp Q
xuôi ngược migration
command tạo dữ liệu mẫu 


(venv) C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorial>python manage.py startapp blog

(venv) C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorial>python manage.py makemigrations blog
Migrations for 'blog':
  blog\migrations\0001_initial.py
    + Create model Author
    + Create model Post
    + Create model Comment

(venv) C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorial>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, debug_toolbar, polls, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK     
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK   
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying blog.0001_initial... OK
  Applying debug_toolbar.0001_initial... OK
  Applying polls.0001_initial... OK
  Applying sessions.0001_initial... OK

(venv) C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorial>python manage.py migrate blog zero   # xóa toàn bộ bảng của app blog
usage: manage.py migrate [-h] [--noinput]
                         [--database {default}] [--fake]
                         [--fake-initial] [--plan]
                         [--run-syncdb] [--check] [--prune]      
                         [--version] [-v {0,1,2,3}]
                         [--settings SETTINGS]
                         [--pythonpath PYTHONPATH]
                         [--traceback] [--no-color]
                         [--force-color] [--skip-checks]
                         [app_label] [migration_name]
manage.py migrate: error: unrecognized arguments: # xóa toàn bộ bảng của app blog

(venv) C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorial># hoặc
'#' is not recognized as an internal or external command,        
operable program or batch file.

(venv) C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorial>python manage.py migrate blog 0001   # quay về migration số 0001

usage: manage.py migrate [-h] [--noinput]
                         [--database {default}] [--fake]
                         [--fake-initial] [--plan]
                         [--run-syncdb] [--check] [--prune]      
                         [--version] [-v {0,1,2,3}]
                         [--settings SETTINGS]
                         [--pythonpath PYTHONPATH]
                         [--traceback] [--no-color]
                         [--force-color] [--skip-checks]
                         [app_label] [migration_name]
manage.py migrate: error: unrecognized arguments: # quay về migration số 0001

(venv) C:\Users\Admin\Desktop\Ky9\ChuyenDeCongNghe\djangotutorial>python manage.py shell
12 objects imported automatically (use -v 2 for details).

Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Author, Post, Comment
>>>
>>> # Tạo tác giả
>>> a1 = Author.objects.create(name="Alice", email="alice@example.com")
>>> a2 = Author.objects.create(name="Bob", email="bob@example.com")
>>>
>>> # Tạo bài viết
>>> p1 = Post.objects.create(title="Hello Django", content="Django is cool!", author=a1)
>>> p2 = Post.objects.create(title="Second Post", content="Learning ORM", author=a2)
>>>
>>> # Tạo comment
>>> Comment.objects.create(post=p1, author="Tom", text="Great post!")
<Comment: Comment by Tom>
>>> Comment.objects.create(post=p1, author="Jerry", text="Thanks for sharing")
<Comment: Comment by Jerry>
>>> # Lấy tất cả bài viết của Alice
>>> alice_posts = Post.objects.filter(author__name="Alice")
>>>
>>> # Lấy comment của 1 bài viết
>>> comments = p1.comments.all()
>>> from django.db.models import Q
>>>
>>> # Tìm post có title chứa "Django" hoặc content chứa "ORM"
>>> posts = Post.objects.filter(Q(title__icontains="Django") | Q(content__icontains="ORM"))
>>>
>>> # Tìm post không phải của Alice
>>> not_alice = Post.objects.filter(~Q(author__name="Alice"))
>>>