using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ST10365068_CLDV_6212_CLOUD_PART_1.Data;
using ST10365068_CLDV_6212_CLOUD_PART_1.Models;
using ST10365068_CLDV_6212_CLOUD_PART_1.Services;

namespace ST10365068_CLDV_6212_CLOUD_PART_1.Controllers
{
    public class ProductsController : Controller
    {
        private readonly ApplicationDbContext _context;
        private readonly AzureProductsQueueService _queueService;

        public ProductsController(ApplicationDbContext context, AzureProductsQueueService queueService)
        {
            _context = context;
            _queueService = queueService;
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create(Products product)
        {
            if (ModelState.IsValid)
            {
                _context.Products.Add(product);
                await _context.SaveChangesAsync();
                await _queueService.SendMessageAsync(product);
                return RedirectToAction(nameof(Success));
            }
            return View(product);
        }

        public async Task<IActionResult> Index()
        {
            var products = await _context.Products.ToListAsync();
            return View(products);
        }

        public IActionResult Success()
        {
            return View();
        }
    }
}
