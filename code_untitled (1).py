print("بررسی قدرت پسورد")
password = input("پسورد را وارد کنید: ")

if len(password) < 6:
    print("خیلی ضعیف ❌")
elif password.isalpha() or password.isdigit():
    print("متوسط ⚠️")
else:
    print("قوی ✅")