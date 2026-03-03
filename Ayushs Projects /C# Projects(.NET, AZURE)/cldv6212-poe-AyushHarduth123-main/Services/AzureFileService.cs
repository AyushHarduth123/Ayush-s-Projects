using Azure;
using Azure.Storage.Files.Shares;

namespace ST10365068_CLDV_6212_CLOUD_PART_1.Services
{
    public class AzureFileService
    {
        private readonly string _storageAccountName;
        private readonly string _fileShareName;
        private readonly string _storageAccountKey;

        public AzureFileService(string storageAccountName, string fileShareName, string storageAccountKey)
        {
            _storageAccountName = storageAccountName;
            _fileShareName = fileShareName;
            _storageAccountKey = storageAccountKey;
        }

        public async Task UploadFileAsync(string fileName, byte[] content, string description)
        {
            string shareUri = $"https://{_storageAccountName}.file.core.windows.net/{_fileShareName}";

            ShareClient share = new ShareClient(new Uri(shareUri), new Azure.Storage.StorageSharedKeyCredential(_storageAccountName, _storageAccountKey));

            ShareDirectoryClient directory = share.GetRootDirectoryClient();
            ShareFileClient file = directory.GetFileClient(fileName);

            using (MemoryStream stream = new MemoryStream(content))
            {
                await file.CreateAsync(stream.Length);
                await file.UploadRangeAsync(new HttpRange(0, stream.Length), stream);
            }

            // Optionally, you can store the description in a metadata or a separate file
            ShareFileClient descriptionFile = directory.GetFileClient($"{fileName}_description.txt");
            byte[] descriptionBytes = System.Text.Encoding.UTF8.GetBytes(description);
            using (MemoryStream descriptionStream = new MemoryStream(descriptionBytes))
            {
                await descriptionFile.CreateAsync(descriptionStream.Length);
                await descriptionFile.UploadRangeAsync(new HttpRange(0, descriptionStream.Length), descriptionStream);
            }
        }
    }
}
