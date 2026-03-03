using Microsoft.AspNetCore.Mvc.Rendering;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace ST10365068_CLDV_6212_CLOUD_PART_1.Models
{
    public class OrderViewModel
    {
        [Required]
        public int CustomerID { get; set; }

        [Required]
        public string CustomerName { get; set; }

        [Required]
        public int ProductID { get; set; }

        [Required]
        public string Product { get; set; }

        [Required]
        [Range(1, int.MaxValue, ErrorMessage = "Quantity must be greater than 0")]
        public int Quantity { get; set; }

        public List<SelectListItem> Customers { get; set; }
        public List<SelectListItem> Products { get; set; }
    }
}
