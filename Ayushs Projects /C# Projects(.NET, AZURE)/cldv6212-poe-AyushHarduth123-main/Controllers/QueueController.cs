using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.AspNetCore.Mvc;
using ST10365068_CLDV_6212_CLOUD_PART_1.Data;
using ST10365068_CLDV_6212_CLOUD_PART_1.Models;
using ST10365068_CLDV_6212_CLOUD_PART_1.Services;
using Microsoft.EntityFrameworkCore;

public class QueueController : Controller
{
    private readonly ApplicationDbContext _context;
    private readonly AzureOrdersQueueService _queueService;

    public QueueController(ApplicationDbContext context, AzureOrdersQueueService queueService)
    {
        _context = context;
        _queueService = queueService;
    }

    public async Task<IActionResult> Queue()
    {
        var customers = await _context.Customers
            .Select(c => new SelectListItem
            {
                Value = c.CustomerID.ToString(),
                Text = c.Name + " " + c.Surname
            }).ToListAsync();

        var products = await _context.Products
            .Select(p => new SelectListItem
            {
                Value = p.ProductID.ToString(),
                Text = p.ProductName
            }).ToListAsync();

        var viewModel = new OrderViewModel
        {
            Customers = customers,
            Products = products
        };

        return View(viewModel); // Ensure this is pointing to the correct view
    }

    [HttpPost]
    public async Task<IActionResult> Create(OrderViewModel viewModel)
    {
        Console.WriteLine("Form submission received");

        // Log the values
        Console.WriteLine($"CustomerID: {viewModel.CustomerID}");
        Console.WriteLine($"ProductID: {viewModel.ProductID}");
        Console.WriteLine($"Quantity: {viewModel.Quantity}");

        if (ModelState.IsValid)
        {
            Console.WriteLine("Model state is valid");

            var customer = await _context.Customers.FindAsync(viewModel.CustomerID);
            var product = await _context.Products.FindAsync(viewModel.ProductID);

            if (customer == null || product == null)
            {
                Console.WriteLine("Invalid customer or product");
                ModelState.AddModelError(string.Empty, "Invalid customer or product.");

                viewModel.Customers = await _context.Customers
                    .Select(c => new SelectListItem
                    {
                        Value = c.CustomerID.ToString(),
                        Text = c.Name + " " + c.Surname
                    }).ToListAsync();

                viewModel.Products = await _context.Products
                    .Select(p => new SelectListItem
                    {
                        Value = p.ProductID.ToString(),
                        Text = p.ProductName
                    }).ToListAsync();

                return View("Queue", viewModel); // Explicitly look for the Queue view
            }

            // Set CustomerName and Product fields for the view model
            viewModel.CustomerName = customer.Name + " " + customer.Surname;
            viewModel.Product = product.ProductName;

            var order = new Order
            {
                CustomerID = viewModel.CustomerID,
                CustomerName = viewModel.CustomerName,
                ProductID = viewModel.ProductID,
                Product = viewModel.Product,
                Quantity = viewModel.Quantity
            };

            try
            {
                _context.Orders.Add(order);
                Console.WriteLine("Order added to context");
                await _context.SaveChangesAsync();
                Console.WriteLine("Order saved to database");
                await _queueService.SendMessageAsync(order); // Send the order to the queue
                Console.WriteLine("Order sent to queue");

                ViewBag.Message = "Order created successfully and added to the queue!";
                Console.WriteLine("Redirecting to Success view");
                return RedirectToAction(nameof(Success));
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error saving order: {ex.Message}");
                ModelState.AddModelError(string.Empty, "An error occurred while creating the order.");
            }
        }
        else
        {
            Console.WriteLine("Model state is invalid");

            // Log ModelState errors
            var errors = ModelState.Values.SelectMany(v => v.Errors);
            foreach (var error in errors)
            {
                Console.WriteLine($"Model state error: {error.ErrorMessage}");
            }
        }

        // Repopulate dropdowns if the model state is invalid
        viewModel.Customers = await _context.Customers
            .Select(c => new SelectListItem
            {
                Value = c.CustomerID.ToString(),
                Text = c.Name + " " + c.Surname
            }).ToListAsync();

        viewModel.Products = await _context.Products
            .Select(p => new SelectListItem
            {
                Value = p.ProductID.ToString(),
                Text = p.ProductName
            }).ToListAsync();

        Console.WriteLine("Returning to Queue view with invalid model state");
        return View("Queue", viewModel); // Explicitly look for the Queue view
    }

    public IActionResult Success()
    {
        Console.WriteLine("Success view triggered");
        return View();
    }
}



