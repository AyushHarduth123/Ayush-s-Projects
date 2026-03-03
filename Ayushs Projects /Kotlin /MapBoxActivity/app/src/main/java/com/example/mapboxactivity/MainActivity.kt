package com.example.mapboxactivity

import android.annotation.SuppressLint
import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import com.mapbox.geojson.Point
import com.mapbox.maps.CameraOptions
import com.mapbox.maps.MapView
import com.mapbox.maps.Style
import com.mapbox.maps.plugin.attribution.attribution
import com.mapbox.maps.plugin.compass.compass
import com.mapbox.maps.plugin.locationcomponent.location
import com.mapbox.maps.plugin.logo.logo
import com.mapbox.maps.plugin.viewport.viewport
import com.mapbox.maps.plugin.viewport.data.FollowPuckViewportStateOptions
import com.mapbox.android.core.permissions.PermissionsListener
import com.mapbox.android.core.permissions.PermissionsManager

class MainActivity : ComponentActivity(), PermissionsListener {

    private lateinit var mapView: MapView
    private lateinit var permissionsManager: PermissionsManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Create a MapView programmatically
        mapView = MapView(this)

        // Set initial camera
        mapView.mapboxMap.setCamera(
            CameraOptions.Builder()
                .center(Point.fromLngLat(-98.0, 39.5))
                .zoom(2.0)
                .pitch(0.0)
                .bearing(0.0)
                .build()
        )

        mapView.mapboxMap.loadStyle(Style.STANDARD) {
            handleLocationPermission()
        }

        // Keep attribution/logo/compass visible to meet Mapbox conditions
        mapView.attribution.enabled = true
        mapView.logo.enabled = true
        mapView.compass.enabled = true

        setContentView(mapView)
    }

    /** Check & request location permissions **/
    private fun handleLocationPermission() {
        if (PermissionsManager.areLocationPermissionsGranted(this)) {
            enableUserLocation()
        } else {
            permissionsManager = PermissionsManager(this)
            permissionsManager.requestLocationPermissions(this)
        }
    }

    override fun onRequestPermissionsResult(
        requestCode: Int, permissions: Array<String>, grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        permissionsManager.onRequestPermissionsResult(requestCode, permissions, grantResults)
    }

    override fun onExplanationNeeded(permissionsToExplain: List<String>) {
        Toast.makeText(
            this,
            "This app needs location permissions to show your position.",
            Toast.LENGTH_LONG
        ).show()
    }

    override fun onPermissionResult(granted: Boolean) {
        if (granted) {
            enableUserLocation()
        } else {
            Toast.makeText(this, "Location permission denied.", Toast.LENGTH_LONG).show()
        }
    }

    /** Enable Mapbox location puck **/
    @SuppressLint("MissingPermission")
    private fun enableUserLocation() {
        mapView.location.updateSettings {
            enabled = true
            pulsingEnabled = true // optional nice effect
        }

        // Make camera follow the user’s location
        mapView.viewport.transitionTo(
            mapView.viewport.makeFollowPuckViewportState(
                FollowPuckViewportStateOptions.Builder().build()
            )
        )
    }

    /** Forward lifecycle events to MapView **/
    override fun onStart() {
        super.onStart()
        mapView.onStart()
    }

    override fun onStop() {
        super.onStop()
        mapView.onStop()
    }

    override fun onLowMemory() {
        super.onLowMemory()
        mapView.onLowMemory()
    }

    override fun onDestroy() {
        super.onDestroy()
        mapView.onDestroy()
    }
}
