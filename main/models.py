from django.db import models




class Art(models.Model):
    title = models.CharField('Название', max_length=100)
    intro = models.CharField('Анонс',max_length=250)
    price = models.CharField('Цена', max_length=100)
    full_text = models.TextField('статья')
    data = models.DateField('Дата публицации')
    image = models.ImageField(blank=True, help_text='150x150px', verbose_name='Ссылка картинки' )
    
    

    def __str__(self):
        return f"Название: {self.title}"
    
    class Meta:
        verbose_name = "Доска"
        verbose_name_plural = "Доска"