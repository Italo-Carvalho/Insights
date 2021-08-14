from django.core.management.base import BaseCommand
import pandas as pd
from insights.models import Tags, Card
from rich.console import Console
import time
console = Console()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        inicio = time.time()
        df = pd.read_csv('cards.csv', names=['text', 'tag'], header=None)
        tags = df.tag.to_list()
        cards_created = 0
        tags_created = 0
        cards_tags_relations = 0

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
                            cards_tags_relations = cards_tags_relations + 1
                        else:
                            dtag = Tags.objects.create(name=tag)
                            tags_created = tags_created + 1
                            card.tags.add(dtag)
                            cards_tags_relations = cards_tags_relations + 1
        fim = time.time()
        tempo_total = fim - inicio
        style = "bold white on #7100ad"
        style2 = "bold white on black"
        style3 = "bold white on #b52a4a"
        style4 = "bold white on #060a8a"
        console.print("Dados diferentes cadastrados", style=style, justify="center")
        console.print(f"🎴  {cards_created} - Novos card's criados\n🏷️  {tags_created} - Novas tag's criadas \n🤝 {cards_tags_relations} - Novos relacionamentos entre Card e Tags feitos", style=style2, justify="center")
        console.print("🕒 %.2f Tempo de execução" %tempo_total, style=style4, justify="center")




