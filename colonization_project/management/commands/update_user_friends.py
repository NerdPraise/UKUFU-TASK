from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from colonization_project.models import Person

import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('people.json', 'r') as person_data:
            persons = json.load(person_data)
            try:
                for person in persons:
                    person = Person.objects.get(guid=person.get('guid'))
                    friends = person.get('friends')
                    person_friends = (Person.objects.get(pk=(friend.get('index')+1))
                                      for friend in friends)
                    person.friends.set(person_friends)

            except Exception as e:
                raise CommandError(e)

        return self.stdout.write(self.style.SUCCESS('Persons populated'))
