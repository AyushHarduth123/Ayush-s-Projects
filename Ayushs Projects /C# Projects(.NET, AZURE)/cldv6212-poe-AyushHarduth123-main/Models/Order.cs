using System.ComponentModel.DataAnnotations;

namespace ST10365068_CLDV_6212_CLOUD_PART_1.Models
{
    public class Order
    {
        [Key]
        public int OrderID { get; set; }

        [Required]
        public int CustomerID { get; set; }

        [Required]
        public string CustomerName { get; set; }

        [Required]
        public int ProductID { get; set; }

        [Required]
        public string Product { get; set; }

        [Required]
        public int Quantity { get; set; }
    }
}
