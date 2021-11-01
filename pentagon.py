from tqdm import tqdm
from time import sleep
import random

x = input("Введите кого взломать(id аккаунта, имя фамилия и т.п))>> ")
print(f"Взлом {x}")

for i in tqdm(range(1)):
    sleep(random.random())

x = input(f"{x} ВЗЛОМАН! Что сделать? (Сьесть/Дать пароль)>> ").lower()
if x == "сьесть":
    for i in tqdm(range(5)):
        sleep(random.random())
    print(f"{x} успешно съеден")
elif x == "дать пароль":
    print("""Ха-ха, серьезно?. Ты действительно веришь что python программа действительно может взломать какую-то социальную сеть?
Чел иди поспи, а если выспался, посмотри видео топлеса хотябы про хакинг и как это работает...""")
else:
    print("Пиши нормально")

input("press close to exit") 
