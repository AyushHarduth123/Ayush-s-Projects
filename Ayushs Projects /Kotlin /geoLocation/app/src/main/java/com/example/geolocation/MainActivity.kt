package com.example.geolocation  // Replace with your actual package name

import android.Manifest
import android.content.Context
import android.content.pm.PackageManager
import android.location.Location
import android.location.LocationListener
import android.location.LocationManager
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat

class MainActivity : AppCompatActivity(), LocationListener {

    private lateinit var locationManager: LocationManager
    private lateinit var tvGpsLocation: TextView
    private val locationPermissionCode = 2

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        title = "KotlinApp"

        tvGpsLocation = findViewById(R.id.textView)
        val button: Button = findViewById(R.id.getLocation)

        button.setOnClickListener {
            getLocation()
        }
        val backButton: Button = findViewById(R.id.backButton)
        backButton.setOnClickListener {
            // Go back to previous activity
            finish() // 🔙 This finishes the current activity and returns to the previous one
        }

    }

    private fun getLocation() {
        locationManager = getSystemService(Context.LOCATION_SERVICE) as LocationManager

        // Check if either FINE or COARSE location permission is granted
        if (
            ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED &&
            ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED
        ) {
            // Request FINE location permission
            ActivityCompat.requestPermissions(
                this,
                arrayOf(Manifest.permission.ACCESS_FINE_LOCATION),
                locationPermissionCode
            )
            return // 🚫 Prevent execution until permission is granted
        }

        // ✅ Now it's safe to request location updates
        locationManager.requestLocationUpdates(
            LocationManager.GPS_PROVIDER,
            5000L, // 5 seconds
            5f,    // 5 meters
            this
        )
    }


    override fun onLocationChanged(location: Location) {
        tvGpsLocation.text = "Latitude: ${location.latitude}, Longitude: ${location.longitude}"
    }

    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)

        if (requestCode == locationPermissionCode) {
            if (grantResults.isNotEmpty() && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                Toast.makeText(this, "Permission Granted", Toast.LENGTH_SHORT).show()
                getLocation() // Try again now that permission is granted
            } else {
                Toast.makeText(this, "Permission Denied", Toast.LENGTH_SHORT).show()
            }
        }
    }
}
