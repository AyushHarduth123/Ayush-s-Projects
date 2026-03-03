using Microsoft.AspNetCore.Mvc;
using ST10365068_CLDV_6212_CLOUD_PART_1.Models;
using ST10365068_CLDV_6212_CLOUD_PART_1.Services;
using System.Threading.Tasks;

namespace ST10365068_CLDV_6212_CLOUD_PART_1.Controllers
{
    public class CustomerController : Controller
    {
        private readonly CustomerService _customerService;

        public CustomerController(CustomerService customerService)
        {
            _customerService = customerService;
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create(Customer customer)
        {
            if (ModelState.IsValid)
            {
                await _customerService.AddCustomerAsync(customer);
                return RedirectToAction(nameof(Success));
            }
            return View(customer);
        }

        public IActionResult Success()
        {
            return View();
        }
    }
}
