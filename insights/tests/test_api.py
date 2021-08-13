import json
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from ..models import Tags, Card, CustomUser
from ..api.serializes import TagsSerializer, CardSerializer
from rest_framework_simplejwt.tokens import RefreshToken
import pytest



pytestmark = pytest.mark.django_db

# @pytest.fixture
def api_auth_user():
    user = CustomUser.objects.create_user(email='test@test.com', password='passw0rd')
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    
    return client


class CardAPIViewTestCase(APITestCase):
    url_lc = reverse("api:card_lc")
    

    def setUp(self):
        self.user=api_auth_user()
        self.card = Card.objects.create(texto='teste')
        self.card_serializer = CardSerializer(instance=self.card).data

    def test_card_list_create_api(self):
        # GET/POST
        response_get = self.user.get(self.url_lc)
        response_post = self.user.post(self.url_lc, {'texto':'testtext'})
        self.assertEqual(json.loads(response_get.content)['results'][0], self.card_serializer)
        self.assertEqual(response_get.status_code, 200)
        self.assertEqual(response_post.status_code, 201)

    def test_card_retrieve_update_delete_api(self):
        
        url_rud = reverse("api:card_rud", kwargs={'pk': self.card.id})

        # GET
        response_get = self.user.get(url_rud)
        self.assertEqual(response_get.status_code, 200)
        self.assertEqual(json.loads(response_get.content), self.card_serializer)

        # O PUT, é usado para alteração de um dado completo
        # O PATCH é usado para atualização parcial.
        # Como esse projeto não há nenhum campo obrigatorio o teste é o mesmo
        response_put = self.user.put(url_rud, {'texto':'texto moficado'})
        response_patch = self.user.patch(url_rud, {'texto':'texto moficado'})
        self.assertEqual(response_put.status_code, 200)
        self.assertEqual(json.loads(response_put.content)['texto'], 'texto moficado')
        self.assertEqual(response_patch.status_code, 200)
        self.assertEqual(json.loads(response_patch.content)['texto'], 'texto moficado')

        # DELETE
        response_delete1 = self.user.delete(url_rud)
        self.assertEqual(response_delete1.status_code, 204)
        response_delete1 = self.user.delete(url_rud)
        self.assertEqual(response_delete1.status_code, 404)       


class TagsAPIViewTestCase(APITestCase):
    url_c = reverse("api:tags_c")
    

    def setUp(self):
        self.user=api_auth_user()
        self.tag = Tags.objects.create(name='teste')
        self.tag_serializer = TagsSerializer(instance=self.tag).data

    def test_tag_create_api(self):

        # POST/GET(ERROR)
        response_get = self.user.get(self.url_c)
        response_post = self.user.post(self.url_c, {'name':'testname'})

        self.assertEqual(response_get.status_code, 405)
        self.assertEqual(response_post.status_code, 201)

    def test_tag_retrieve_update_delete_api(self):
        
        url_rud = reverse("api:tags_rud", kwargs={'pk': self.tag.id})

        # GET
        response_get = self.user.get(url_rud)
        self.assertEqual(response_get.status_code, 200)
        self.assertEqual(json.loads(response_get.content), self.tag_serializer)

        # PUT/PATCH
        response_put = self.user.put(url_rud, {'name':'Nome moficado'})
        response_patch = self.user.patch(url_rud, {'name':'Nome moficado'})
        self.assertEqual(response_put.status_code, 200)
        self.assertEqual(json.loads(response_put.content)['name'], 'Nome moficado')
        self.assertEqual(response_patch.status_code, 200)
        self.assertEqual(json.loads(response_patch.content)['name'], 'Nome moficado')

        # DELETE
        response_delete1 = self.user.delete(url_rud)
        self.assertEqual(response_delete1.status_code, 204)
        response_delete1 = self.user.delete(url_rud)
        self.assertEqual(response_delete1.status_code, 404)    







 

