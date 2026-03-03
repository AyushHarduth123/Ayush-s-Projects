using ST10365068_CLDV_6212_CLOUD_PART_1.Models;
using ST10365068_CLDV_6212_CLOUD_PART_1.Data;
using System.Threading.Tasks;

namespace ST10365068_CLDV_6212_CLOUD_PART_1.Services
{
    public class CustomerService
    {
        private readonly ApplicationDbContext _context;

        public CustomerService(ApplicationDbContext context)
        {
            _context = context;
        }

        public async Task AddCustomerAsync(Customer customer)
        {
            _context.Customers.Add(customer);
            await _context.SaveChangesAsync();
        }

        // Add more methods for CRUD operations as needed
    }
}
