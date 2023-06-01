from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from food.models import ProductTranslation
from .prompts import prompts
import openai
import asyncio
import backoff


class GPT(AsyncJsonWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']

        if not user.is_authenticated:
            return self.disconnect(close_code=401)

        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive_json(self, content):
        try:
            asyncio.create_task(self.handle(content))
        except openai.error.RateLimitError:
            return await self.send_json({'id': content['id'], 'error': True, 'status': 429})

    @backoff.on_exception(backoff.expo, openai.error.RateLimitError, max_tries=10)
    async def handle(self, content):
        ingredients = content['ingredients']
        handler_id = content['id']
        language = content['lang']
        field = content['field']
        model = content['model']
        title = content['title']

        try:
            prompt = prompts[language][model][field]
        except KeyError:
            return await self.send_json({'id': handler_id, 'error': True})

        if model == 'dish':
            ingredients = await sync_to_async(list)(ProductTranslation.objects.filter(product__in=ingredients, language=language))

        ingredients = [ingredient.title for ingredient in ingredients]

        async for response in await openai.ChatCompletion.acreate(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt.format(title=title, ingredients='\n'.join(ingredients))}],
            stream=True
        ):
            await self.send_json({'id': handler_id, 'message': response.choices[0], 'error': False})
