user_secs = int(input("Print here some seconds:"))
secs = user_secs % 60
mins = (user_secs // 60) % 60
hours = user_secs // 3600
print(f"It is: {hours:02d}:{mins:02d}:{secs:02d}")
