from src.vacancy import Vacancy


def top_vacancies(vacancies: list[Vacancy], top=5):
    """Функция сортировки по зарплате и вывода топа 5 вакансий"""

    return sorted(vacancies, reverse=True)[:top]


def print_vacancies(vacancies: list[Vacancy]):
    """Функция вывода на экран"""
    for vac in vacancies:
        print(vac)
