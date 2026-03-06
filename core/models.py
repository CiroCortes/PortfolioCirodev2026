from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título del Proyecto")
    description = models.TextField(verbose_name="Descripción")
    tech_stack = models.CharField(max_length=200, verbose_name="Tecnologías (Py, JS, etc.)")
    url = models.URLField(blank=True, null=True, verbose_name="Enlace al Proyecto")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name="Imagen")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-created_at']

    @property
    def tech_list(self):
        """Devuelve la tech_stack como lista limpia, separando por '·'."""
        return [t.strip() for t in self.tech_stack.split('·') if t.strip()]

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de Habilidad")
    level = models.CharField(max_length=50, verbose_name="Nivel (Ej. Senior, Junior)")
    category_icon = models.CharField(
        max_length=50, 
        help_text="Nombre del ícono de Material Symbols (ej. 'code', 'android', 'security')",
        verbose_name="Ícono"
    )

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo Electrónico")
    message = models.TextField(verbose_name="Mensaje")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"
        ordering = ['-created_at']

    def __str__(self):
        return f"Mensaje de {self.name} - {self.email}"
