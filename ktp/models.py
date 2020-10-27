from django.db import models


class AcademicYear(models.Model):
    academic_year = models.CharField('Учебный год', max_length=20)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Учебный год'
        verbose_name_plural = 'Учебные года'

    def __str__(self):
        return self.academic_year


class Teacher(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    second_name = models.CharField('Отчество', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    phone = models.CharField('Телефон', max_length=20, blank=True)
    email = models.CharField('Электронная почта', max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
       """ return self.surname + ' ' + self.first_name + ' ' + self.second_name """
       return f"{self.surname} {self.first_name} {self.second_name}"


class SchoolForm(models.Model):
    form_name = models.CharField('Название класса', max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    class_ruk = models.ForeignKey(Teacher, on_delete=models.CASCADE,
                                  verbose_name='Классный руководитель')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __str__(self):
        return self.form_name


class Discipline(models.Model):
    discipline_name = models.CharField('Название дисциплины', max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return self.discipline_name


class KTP(models.Model):
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE,
                                      verbose_name='Учебный год')
    school_form = models.ForeignKey(SchoolForm, on_delete=models.CASCADE,
                                    verbose_name='Класс')
    discipline_name = models.ForeignKey(Discipline, on_delete=models.CASCADE,
                                        verbose_name='Дисциплина')
    number_of_lesson = models.SmallIntegerField(verbose_name='Номер урока')
    plan_date = models.DateField(blank=True, verbose_name='Планируемая дата')
    fact_date = models.DateField(null=True, blank=True, verbose_name='Дата проведения')
    theme = models.TextField(verbose_name='Тема урока')
    home_task = models.CharField('Домашнее задание', max_length=255, null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ("number_of_lesson",)

    def __str__(self):
        return self.theme
