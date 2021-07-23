from django.core.management.base import BaseCommand, CommandError

from colonization_project.models import Company

import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('companies.json', 'r') as company_data:
            companies = json.load(company_data)
            try:
                for company in companies:
                    Company.objects.create(
                        name=company['company'], index=company['index'])

            except (KeyError, IndexError) as e:
                raise BaseCommand(e)

        return self.stdout.write(self.style.SUCCESS('Companies populated'))
