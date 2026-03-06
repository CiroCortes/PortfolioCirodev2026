"""
Management command to seed the database with real portfolio data.
Run: python manage.py seed_portfolio
"""
from django.core.management.base import BaseCommand
from core.models import Project, Skill


class Command(BaseCommand):
    help = 'Seeds the database with real portfolio data from GitHub profile'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        Project.objects.all().delete()
        Skill.objects.all().delete()

        # --- PROJECTS from pinned GitHub repos ---
        projects = [
            {
                'title': 'Asistencias Cristiana App',
                'description': 'App móvil multiplataforma desarrollada con Flutter para una entidad cristiana. Permite registrar asistencia de miembros en tiempo real con sincronización en la nube, diseñada como proyecto freelance en producción activa.',
                'tech_stack': 'Flutter · Dart · Firebase',
                'url': 'https://github.com/CiroCortes/asistencias_cristianaa',
            },
            {
                'title': 'InDrive Clone Android',
                'description': 'Clon funcional de la aplicación InDrive construido con Kotlin siguiendo arquitectura MVVM limpia. Incluye mapas en tiempo real, roles de conductor/pasajero y sincronización con backend Python.',
                'tech_stack': 'Kotlin · Android · MVVM',
                'url': 'https://github.com/CiroCortes/CloneInDriverAndroid',
            },
            {
                'title': 'BrandProduct API',
                'description': 'API REST enterprise construida con Java + Spring Boot para gestionar catálogos de marcas y productos. Arquitectura por capas con operaciones CRUD completas, documentación Swagger y persistencia en base de datos relacional.',
                'tech_stack': 'Java · Spring Boot · REST API',
                'url': 'https://github.com/CiroCortes/BrandProductAPI',
            },
            {
                'title': 'Backend Clone InDrive',
                'description': 'Backend robusto en Python para el sistema InDrive Clone. Expone una API REST que maneja la lógica de negocio de transporte: gestión de viajes, usuarios, drivers y coordenadas en tiempo real.',
                'tech_stack': 'Python · Django · REST API',
                'url': 'https://github.com/CiroCortes/BackendCloneIndrive',
            },
            {
                'title': 'BotReels AI — YT & TikTok',
                'description': '⭐ 2 estrellas — Bot automatizado con IA para la creación y publicación de reels en YouTube y TikTok. Automatiza la generación de contenido multimedia, edición de video y programación de publicaciones sin intervención humana.',
                'tech_stack': 'Python · AI · Automation',
                'url': 'https://github.com/CiroCortes/BotreelsYTTKTK',
            },
            {
                'title': 'Sistema de Pedidos Pesco',
                'description': '⭐ 2 estrellas — Sistema inteligente con IA para la gestión integral de pedidos y despacho para empresa pesquera. Automatiza la emisión, seguimiento y procesamiento de órdenes de compra con clasificación asistida por inteligencia artificial.',
                'tech_stack': 'Python · HTML · AI · Web',
                'url': 'https://github.com/CiroCortes/sistemaPedidosPesco',
            },
        ]

        for p in projects:
            Project.objects.create(**p)
            self.stdout.write(self.style.SUCCESS(f'  [+] Project: {p["title"]}'))

        # --- SKILLS / NEURAL IMPLANTS ---
        skills = [
            {'name': 'Python & Django', 'level': 'Senior Netrunner', 'category_icon': 'code'},
            {'name': 'Kotlin & Android', 'level': 'Mobile Specialist', 'category_icon': 'android'},
            {'name': 'Flutter & Dart', 'level': 'Cross-Platform Dev', 'category_icon': 'phone_iphone'},
            {'name': 'Java & Spring Boot', 'level': 'Backend Architect', 'category_icon': 'hub'},
            {'name': 'AI & Automation', 'level': 'AI Operative', 'category_icon': 'smart_toy'},
            {'name': 'REST APIs & DBs', 'level': 'Data Engineer', 'category_icon': 'storage'},
            {'name': 'PostgreSQL & SQL', 'level': 'Database Specialist', 'category_icon': 'database'},
            {'name': 'Git & GitHub', 'level': 'Version Control Pro', 'category_icon': 'merge_type'},
        ]

        for s in skills:
            Skill.objects.create(**s)
            self.stdout.write(self.style.SUCCESS(f'  [+] Skill: {s["name"]}'))

        self.stdout.write(self.style.SUCCESS('\n✅ PORTFOLIO SEEDED SUCCESSFULLY. All systems operational.'))
