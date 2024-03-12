from flask import Flask, request, jsonify
import discord
from discord.ext import commands
import os

app = Flask(__name__)
bot = commands.Bot(command_prefix='!')

# Discord Webhook URL
discord_webhook_url = "https://discord.com/api/webhooks/1217052519365345442/Mb_o3YP6a7vcql4gHF1xrUcqeAZS3oXa2t22iTZHIAIqReVv_8jnCQsqDM0BrH1E3Vor"

@app.route('/webhook', methods=['POST'])
def asana_webhook():
    data = request.json

    # Обработка данных от Asana
    # Допустим, вы хотите отправить в Discord информацию о новой задаче в Asana
    task_name = data['resource']['name']
    project_name = data['resource']['projects'][0]['name']

    # Отправка сообщения в Discord
    discord_message = f'Новая задача в проекте {project_name}: {task_name}'

    webhook = discord.Webhook.from_url(discord_webhook_url, adapter=discord.RequestsWebhookAdapter())
    webhook.send(discord_message)

    return jsonify({'success': True})

if __name__ == '__main__':
    # Запуск Flask-приложения
    app.run(port=int(os.environ.get('PORT', 5000)))
