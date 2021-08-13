from django.core.management.base import BaseCommand
import pandas as pd
from insights.models import Tags, Card
from django.core.management import call_command
from rich.console import Console
from django.core.management.color import no_style
from django.db import connection
console = Console()





class Command(BaseCommand):
    def handle(self, *args, **kwargs):
       
        df = pd.read_csv('cards.csv', names=['text', 'tag'], header=None)
        tags = df.tag.to_list()
        cards_db = []
        tags_db = []
        cards_tags_db = []

        try:
            cards_id = Card.objects.latest('id').id + 1
        except Card.DoesNotExist:
            sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Card])
            with connection.cursor() as cursor:
                for sql in sequence_sql:
                    cursor.execute(sql)
            cards_id = 1

        try:
            tag_id = Tags.objects.latest('id').id
        except Tags.DoesNotExist:
            sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Tags])
            with connection.cursor() as cursor:
                for sql in sequence_sql:
                    cursor.execute(sql)
            tag_id = 0

        for text, tag in zip(df.text, tags):
            tags = list(str(tag).split(";"))
            cards_db.append({'texto':text})

            for tag in tags:
                if tag != 'nan':
                    if {'name':tag} not in tags_db:
                        tags_db.append({'name':tag})
                    tag_id_index = tags_db.index({'name':tag})
                    cards_tags_db.append({'card_id':cards_id, 'tags_id':tag_id_index+tag_id+1})
            cards_id = cards_id + 1


        card_sv = Card.objects.bulk_create([Card(**card) for card in cards_db])
        tags_sv = Tags.objects.bulk_create([Tags(**tag) for tag in tags_db])
        card_tags_sv = Card.tags.through.objects.bulk_create([Card.tags.through(**card_tag) for card_tag in cards_tags_db])

        style = "bold white on purple"
        style2 = "bold white on black"
        style3 = "bold white on red"
        console.print("Dados cadastrados", style=style, justify="center")
        console.print("(!) Esses dados não foram validados, verique no banco de dados se algum dado repetido foi cadastrado!", style=style3, justify="center")
        console.print(f"{len(card_sv)} - Cards criados\n{len(tags_sv)} - Tags cridas\n{len(card_tags_sv)} - Relacionamentos entre Card e Tags fetios", style=style2, justify="center")

        


                





                
                
            




