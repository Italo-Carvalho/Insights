from django.core.management.base import BaseCommand
import pandas as pd
from insights.models import Tags, Card
from rich.console import Console

console = Console()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
       
        df = pd.read_csv('cards.csv', names=['text', 'tag'], header=None)
        tags = df.tag.to_list()
        cards_created = 0
        tags_created = 0

        for text, tag in zip(df.text, tags):
            tags = list(str(tag).split(";"))
            

            if not Card.objects.filter(texto=text).count():
                tags = list(str(tag).split(";"))

                card = Card(texto=text)
                card.save()
                cards_created = cards_created + 1

                for tag in tags:
                    if tag != 'nan':
                        dtag = Tags.objects.filter(name=tag).last()
                        if dtag:
                            card.tags.add(dtag)
                        else:
                            dtag = Tags.objects.create(name=tag)
                            tags_created = tags_created + 1
                            card.tags.add(dtag)
                            
        style = "bold white on purple"
        style2 = "bold white on black"
        console.print("Dados diferentes cadastrados", style=style, justify="center")
        console.print(f"{tags_created} - Tag's criadas \n{cards_created} - Card's criados", style=style2, justify="center")




