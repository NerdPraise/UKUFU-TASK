from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from colonization_project.models import Company, Person

import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('people.json', 'r') as person_data:
            persons = json.load(person_data)
            try:
                for person in persons:
                    user_company = Company.objects.get(
                        pk=person.get('company_id'))
                    Person.objects.create(
                        username=person.get('name'),
                        email=person.get('email'),
                        company=user_company,
                        guid=person.get('guid'),
                        has_died=person.get('has_died'),
                        balance=person.get('balance'),
                        picture=person.get('picture'),
                        age=person.get('age'),
                        eye_color=person.get('eyeColor'),
                        gender=person.get('gender'),
                        about=person.get('about'),
                        registered=person.get('registered'),
                        address=person.get('address'),
                        phone=person.get('phone'),
                        greeting=person.get('greeting'),
                    )

            except Exception as e:
                raise CommandError(e)

        return self.stdout.write(self.style.SUCCESS('Persons populated'))
