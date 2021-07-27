from django.core.management.base import BaseCommand, CommandError

from colonization_project.models import Person

import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('people.json', 'r') as person_data:
            persons = json.load(person_data)
            try:
                for person in persons:
                    current_person = Person.objects.get(
                        guid=person.get('guid'))
                    friends = person.get('friends')

                    person_friends = [Person.objects.get(pk=(friend.get('index')+1))
                                      for friend in friends]
                    current_person.friend.add(*person_friends)
                    current_person.save()

            except Exception as e:
                raise CommandError(e)

        return self.stdout.write(self.style.SUCCESS('Friends updated'))
