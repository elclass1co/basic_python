# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:

# до минуты: <s> сек;
# * до часа: <m> мин <s> сек;
# * до суток: <h> час <m> мин <s> сек;
# * *до месяца, до года, больше года: по аналогии.

duration = int(input('Введите продолжительность в секундах: '))
days = duration // 86400
if days > 0:
    duration = duration - (86400 * days)
hours = duration // 3600
if hours > 0:
    duration = duration - (3600 * hours)
minutes = duration // 60
if minutes > 0:
    duration = duration - (60 * minutes)
seconds = duration
print(f"Дн {days}, час {hours}, мин {minutes}, сек {seconds}")
