using System.ComponentModel.DataAnnotations;

namespace ST10365068_CLDV_6212_CLOUD_PART_1.Models
{
    public class Products
    {
        [Key]
        public int ProductID { get; set; }

        [Required]
        public string ProductName { get; set; }

        [Required]
        public string Description { get; set; }

        [Required]
        [DataType(DataType.Currency)]
        public decimal Price { get; set; }

        [Required]
        public string Category { get; set; }

        [Required]
        public int Quantity { get; set; }
    }
}
