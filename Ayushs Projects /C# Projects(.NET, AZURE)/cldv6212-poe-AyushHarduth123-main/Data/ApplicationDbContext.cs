using Microsoft.EntityFrameworkCore;
using ST10365068_CLDV_6212_CLOUD_PART_1.Models;


namespace ST10365068_CLDV_6212_CLOUD_PART_1.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }

        public DbSet<Customer> Customers { get; set; }
        public DbSet<Order> Orders { get; set; }
        public DbSet<Products> Products { get; set; }
    }
}


