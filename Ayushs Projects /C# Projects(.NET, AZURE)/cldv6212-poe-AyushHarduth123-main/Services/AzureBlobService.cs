using Azure.Storage.Blobs;

namespace ST10365068_CLDV_6212_CLOUD_PART_1.Services
{
    public class AzureBlobService
    {
        private readonly Lazy<BlobServiceClient> _blobServiceClient;

        // Lazy: the Blob client is only created when a file is uploaded, so pages that
        // use this service still open when Blob storage isn't configured
        public AzureBlobService(Lazy<BlobServiceClient> blobServiceClient)
        {
            _blobServiceClient = blobServiceClient;
        }

        public async Task<string> UploadFileAsync(IFormFile file, string containerName)
        {
            var containerClient = _blobServiceClient.Value.GetBlobContainerClient(containerName);
            await containerClient.CreateIfNotExistsAsync();
            var blobClient = containerClient.GetBlobClient(file.FileName);

            await using (var stream = file.OpenReadStream())
            {
                await blobClient.UploadAsync(stream, true);
            }

            return blobClient.Uri.ToString();
        }

    }
}
