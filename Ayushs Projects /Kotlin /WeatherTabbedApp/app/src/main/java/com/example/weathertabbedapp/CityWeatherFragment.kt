package com.example.weathertabbedapp

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.fragment.app.Fragment
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class CityWeatherFragment : Fragment() {

    private lateinit var cityInput: EditText
    private lateinit var searchButton: Button
    private lateinit var resultText: TextView

    private val apiKey = "YOUR_ACCUWEATHER_API_KEY"

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        val root = inflater.inflate(R.layout.fragment_city_weather, container, false)

        cityInput = root.findViewById(R.id.cityEditText)
        searchButton = root.findViewById(R.id.searchButton)
        resultText = root.findViewById(R.id.resultText)

        searchButton.setOnClickListener {
            val cityName = cityInput.text.toString().trim()
            if (cityName.isNotEmpty()) {
                searchCity(cityName)
            } else {
                resultText.text = "Please enter a city name."
            }
        }

        return root
    }

    private fun searchCity(city: String) {
        RetrofitClient.instance.getLocationKey(city, apiKey)
            .enqueue(object : Callback<List<LocationResponse>> {
                override fun onResponse(
                    call: Call<List<LocationResponse>>,
                    response: Response<List<LocationResponse>>
                ) {
                    if (response.isSuccessful && response.body()?.isNotEmpty() == true) {
                        val location = response.body()!![0]
                        resultText.text = "Location Key: ${location.Key}\nCity: ${location.LocalizedName}"
                    } else {
                        resultText.text = "City not found."
                    }
                }

                override fun onFailure(call: Call<List<LocationResponse>>, t: Throwable) {
                    resultText.text = "Failed: ${t.message}"
                }
            })
    }

    private var param1: String? = null
    private var param2: String? = null

    companion object {
        private const val ARG_PARAM1 = "param1"
        private const val ARG_PARAM2 = "param2"

        @JvmStatic
        fun newInstance(param1: String, param2: String) =
            CityWeatherFragment().apply {
                arguments = Bundle().apply {
                    putString(ARG_PARAM1, param1)
                    putString(ARG_PARAM2, param2)
                }
            }
    }
}
