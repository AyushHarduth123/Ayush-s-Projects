
using Azure.Storage.Queues;
using System.Text.Json;

namespace ST10365068_CLDV_6212_CLOUD_PART_1.Services
{
    public class AzureOrdersQueueService
    {
        private readonly QueueClient? _queueClient;

        public AzureOrdersQueueService(string connectionString, string queueName)
        {
            // Don't contact Azure at startup, so the site still opens when Azure isn't set up or reachable.
            // The queue is created (if needed) the first time a message is sent.
            try { _queueClient = new QueueClient(connectionString, queueName); }
            catch (Exception ex) { Console.WriteLine($"Azure queue '{queueName}' is not configured: {ex.Message}"); }
        }

        public async Task SendMessageAsync<T>(T message)
        {
            if (_queueClient == null)
                throw new InvalidOperationException("Azure Queue storage is not configured. Add your connection string to appsettings.Local.json.");

            await _queueClient.CreateIfNotExistsAsync();
            {
                string messageText = JsonSerializer.Serialize(message);
                await _queueClient.SendMessageAsync(Convert.ToBase64String(System.Text.Encoding.UTF8.GetBytes(messageText)));

            }
        }
    }
}
