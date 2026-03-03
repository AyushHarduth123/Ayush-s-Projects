package com.example.acuuweatherapp

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Bundle
import android.util.Log
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.acuuweatherapp.databinding.ActivityMainBinding
import com.google.android.gms.location.FusedLocationProviderClient
import com.google.android.gms.location.LocationServices
import org.json.JSONException
import org.json.JSONObject
import java.net.URL
import kotlin.concurrent.thread

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var fusedLocationClient: FusedLocationProviderClient
    private val fiveDayList = mutableListOf<Forecast>()

    private val LOCATION_PERMISSION_REQUEST_CODE = 1001
    private val LOG_TAG = "WeatherApp"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        ViewCompat.setOnApplyWindowInsetsListener(binding.root) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        fusedLocationClient = LocationServices.getFusedLocationProviderClient(this)

        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION)
            != PackageManager.PERMISSION_GRANTED
        ) {
            ActivityCompat.requestPermissions(
                this,
                arrayOf(Manifest.permission.ACCESS_FINE_LOCATION),
                LOCATION_PERMISSION_REQUEST_CODE
            )
        } else {
            fetchLocation()
        }

        binding.ivAccuweather.setOnClickListener {
            val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://www.accuweather.com/"))
            startActivity(intent)
        }
    }

    private fun fetchLocation() {
        fusedLocationClient.lastLocation.addOnSuccessListener { location ->
            if (location != null) {
                val latitude = location.latitude
                val longitude = location.longitude
                binding.tvLocation.text = "Lat: %.4f, Lon: %.4f".format(latitude, longitude)
                fetchLocationKey(latitude, longitude)
            } else {
                binding.tvLocation.text = "Location unavailable"
            }
        }
    }

    private fun fetchLocationKey(lat: Double, lon: Double) {
        thread {
            val geoUrl =
                "https://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=${BuildConfig.ACCUWEATHER_API_KEY}&q=$lat,$lon"
            val geoJson = try {
                URL(geoUrl).readText()
            } catch (e: Exception) {
                e.printStackTrace()
                return@thread
            }

            runOnUiThread {
                try {
                    val geoData = JSONObject(geoJson)
                    val locationKey = geoData.getString("Key")
                    val locationName = geoData.getString("LocalizedName")
                    binding.tvLocation.text =
                        "$locationName\nLat: %.4f, Lon: %.4f".format(lat, lon)
                    fetchWeather(locationKey)
                } catch (e: JSONException) {
                    e.printStackTrace()
                }
            }
        }
    }

    private fun fetchWeather(locationKey: String) {
        thread {
            val weatherUrl =
                "https://dataservice.accuweather.com/forecasts/v1/daily/5day/$locationKey?apikey=${BuildConfig.ACCUWEATHER_API_KEY}&metric=true"
            val weatherJson = try {
                URL(weatherUrl).readText()
            } catch (e: Exception) {
                e.printStackTrace()
                return@thread
            }

            runOnUiThread {
                consumeJson(weatherJson)
                binding.tvWeather.text = fiveDayList.joinToString("\n") {
                    "Date: ${it.date}, Min: ${it.minimumTemperature}°C, Max: ${it.maximumTemperature}°C"
                }
            }
        }
    }

    private fun consumeJson(weatherJSON: String?) {
        fiveDayList.clear()

        if (weatherJSON != null) {
            try {
                val rootWeatherData = JSONObject(weatherJSON)
                val dailyForecasts = rootWeatherData.getJSONArray("DailyForecasts")

                for (i in 0 until dailyForecasts.length()) {
                    val forecastObject = Forecast()
                    val dailyWeather = dailyForecasts.getJSONObject(i)

                    forecastObject.date = dailyWeather.getString("Date")

                    val temperatureObject = dailyWeather.getJSONObject("Temperature")
                    forecastObject.minimumTemperature =
                        temperatureObject.getJSONObject("Minimum").getString("Value")
                    forecastObject.maximumTemperature =
                        temperatureObject.getJSONObject("Maximum").getString("Value")

                    fiveDayList.add(forecastObject)
                }
            } catch (e: JSONException) {
                e.printStackTrace()
            }
        }
    }
}
