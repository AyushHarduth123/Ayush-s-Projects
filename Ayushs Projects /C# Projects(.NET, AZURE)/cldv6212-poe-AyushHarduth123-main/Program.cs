using Azure.Storage.Blobs;
using Microsoft.EntityFrameworkCore;
using ST10365068_CLDV_6212_CLOUD_PART_1.Services;
using ST10365068_CLDV_6212_CLOUD_PART_1.Data;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

// Register DbContext with SQL Server provider
builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

var connectionString = builder.Configuration.GetConnectionString("AzureQueueConnectionString");

var queueName = builder.Configuration["AzureQueueSettings:QueueName"];
var secondqueueName = builder.Configuration["AzureQueueSettings:ProductsQueueName"];
var customerqueueName = builder.Configuration["AzureQueueSettings:CustomerQueueName"];

string storageAccountName = builder.Configuration["AzureFileStorage:AccountName"];
string fileShareName = builder.Configuration["AzureFileStorage:FileShareName"];
string storageAccountKey = builder.Configuration["AzureFileStorage:AccountKey"]; // Note the corrected casing here

builder.Services.AddSingleton(new AzureOrdersQueueService(connectionString, queueName));
builder.Services.AddSingleton(new AzureCustomerQueueService(connectionString, customerqueueName));
builder.Services.AddSingleton(new AzureProductsQueueService(connectionString, secondqueueName));
builder.Services.AddSingleton(new AzureFileService(storageAccountName, fileShareName, storageAccountKey));
builder.Services.AddScoped<CustomerService>();

var blobServiceClient = new BlobServiceClient(builder.Configuration.GetConnectionString("AzureBlobStorage"));
builder.Services.AddSingleton(blobServiceClient);
builder.Services.AddScoped<AzureBlobService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
