using Microsoft.AspNetCore.Mvc;
using ST10365068_CLDV_6212_CLOUD_PART_1.Models;
using ST10365068_CLDV_6212_CLOUD_PART_1.Services;

using System.Diagnostics;

namespace ST10365068_CLDV_6212_CLOUD_PART_1.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly AzureBlobService _azureBlobService;

        public HomeController(ILogger<HomeController> logger, AzureBlobService azureBlobService)
        {
            _logger = logger;
            _azureBlobService = azureBlobService;
        }

        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> Index(IFormFile file)
        {
            if (file != null)
            {
                var result = await _azureBlobService.UploadFileAsync(file, "storagecontainer");
                ViewBag.Message = "Uploaded successfully!";
            }

            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
