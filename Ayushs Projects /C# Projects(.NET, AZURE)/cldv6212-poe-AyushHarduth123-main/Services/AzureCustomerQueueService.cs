using Azure.Storage.Queues;
using Microsoft.AspNetCore.Mvc;
using System.Text.Json;

namespace ST10365068_CLDV_6212_CLOUD_PART_1.Services
{
    public class AzureCustomerQueueService : Controller
    {
        private readonly QueueClient _queueClient;

        public AzureCustomerQueueService(string connectionString, string customerqueueName)
        {
            _queueClient = new QueueClient(connectionString, customerqueueName);
            _queueClient.CreateIfNotExists();
        }

        public async Task SendMessageAsync<T>(T message)
        {
            if (_queueClient.Exists())
            {
                string messageText = JsonSerializer.Serialize(message);
                await _queueClient.SendMessageAsync(Convert.ToBase64String(System.Text.Encoding.UTF8.GetBytes(messageText)));

            }
        }
    }
}
