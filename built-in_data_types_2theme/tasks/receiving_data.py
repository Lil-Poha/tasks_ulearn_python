def dict_type(a):
    return f" ({type(a).__name__})"


x = input('Введите название вакансии: ')
y = input('Введите описание вакансии: ')
z = input("Введите город для вакансии: ")
v = int(input("Введите требуемый опыт работы (лет): "))
u = int(input("Введите нижнюю границу оклада вакансии: "))
e = int(input("Введите верхнюю границу оклада вакансии: "))
l = input("Нужен свободный график (да / нет): ")
k = input("Является ли данная вакансия премиум-вакансией (да / нет): ")

dict_fraze = {x: dict_type(x), y: dict_type(y), z: dict_type(z),
              v: dict_type(v), u: dict_type(u), e: dict_type(e),
              l: dict_type(l), k: dict_type(k)}
print(str(x) + dict_fraze[x])
print(str(y) + dict_fraze[y])
print(str(z) + dict_fraze[z])
print(str(v) + dict_fraze[v])
print(str(u) + dict_fraze[u])
print(str(e) + dict_fraze[e])

print(f'{"да" == l}{dict_type("да" == l)}')
print(f'{"да" == k}{dict_type("да" == k)}')