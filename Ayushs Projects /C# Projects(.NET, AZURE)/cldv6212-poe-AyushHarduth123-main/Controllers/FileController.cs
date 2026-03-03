using Microsoft.AspNetCore.Mvc;
using ST10365068_CLDV_6212_CLOUD_PART_1.Services;


namespace ST10365068_CLDV_6212_CLOUD_PART_1.Controllers
{
    public class FileController : Controller
    {
        private readonly AzureFileService _azureFileService;

        public FileController(AzureFileService azureFileService)
        {
            _azureFileService = azureFileService;
        }

        [HttpGet]
        public IActionResult Upload()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> Upload(IFormFile file, string description)
        {
            if (file == null || file.Length == 0)
            {
                ModelState.AddModelError(string.Empty, "File is required.");
                return View();
            }

            using (var stream = new MemoryStream())
            {
                await file.CopyToAsync(stream);
                var content = stream.ToArray();
                await _azureFileService.UploadFileAsync(file.FileName, content, description);
            }

            ViewBag.Message = "Successfully uploaded!";
            return View();
        }
    }
}
