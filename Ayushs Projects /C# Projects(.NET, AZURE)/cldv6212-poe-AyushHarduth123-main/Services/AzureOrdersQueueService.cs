
using Azure.Storage.Queues;
using System.Text.Json;

namespace ST10365068_CLDV_6212_CLOUD_PART_1.Services
{
    public class AzureOrdersQueueService
    {
        private readonly QueueClient _queueClient;

        public AzureOrdersQueueService(string connectionString, string queueName)
        {
            _queueClient = new QueueClient(connectionString, queueName);
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
