from django.db import models
from ckeditor.fields import RichTextField
from colorful.fields import RGBColorField

# Create your models here.
class CategoryItem(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(null=True, blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)
    color = RGBColorField()
    link = models.URLField(blank=True, max_length=500)

    class Meta:
        verbose_name_plural = 'Categorias'
        ordering = ['ordering']

    def __str__(self):
        return self.title


class ActivityCategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(CategoryItem, related_name='activity_category', on_delete=models.CASCADE)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categorias de Actividades'
        ordering = ['ordering']

    def __str__(self):
        return "{} - {}".format(self.category.title, self.title)


class Salon(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Salones'

    def __str__(self):
        return self.title


class Actividad(models.Model):
    dress_options = (
        ('n/a', 'N/A',),
        ('formal', 'Formal',),
        ('casual', 'Casual',)
    )
    category = models.ForeignKey(ActivityCategory, related_name='actividades', on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = RichTextField()
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    dress_code = models.CharField('Código de vestir', choices=dress_options, max_length=50)
    academic_program_url = models.URLField('Url Programa Académico', blank=True, max_length=500)
    inscription_url = models.URLField('Url Inscripción', blank=True, max_length=500)
    ordering = models.PositiveSmallIntegerField(default=0)
    month = models.CharField(max_length=50, null=False, blank=True, default='')

    class Meta:
        verbose_name_plural = 'Actividades'
        ordering = ['start_date', 'ordering']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.month = self.start_date.strftime("%B")
        super(Actividad, self).save(*args, **kwargs)


class Presentacion(models.Model):
    actividad = models.ForeignKey(Actividad, related_name='presentaciones', on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=300)
    doctor = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    pdf = models.FileField(null=True, blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Presentaciones'
        ordering = ['ordering']

    def __str__(self):
        return self.title