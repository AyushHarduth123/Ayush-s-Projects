package com.example.weathertabbedapp

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class TodayFragment : Fragment() {

    private lateinit var textView: TextView
    private val apiKey = "YOUR_ACCUWEATHER_API_KEY"
    private val locationKey = "YOUR_LOCATION_KEY" // e.g., "328328" for Johannesburg

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        val root = inflater.inflate(R.layout.fragment_today, container, false)
        textView = root.findViewById(R.id.todayWeatherText)

        RetrofitClient.instance.getTodayWeather(locationKey, apiKey)
            .enqueue(object : Callback<List<WeatherResponse>> {
                override fun onResponse(
                    call: Call<List<WeatherResponse>>,
                    response: Response<List<WeatherResponse>>
                ) {
                    if (response.isSuccessful) {
                        val weather = response.body()?.firstOrNull()
                        weather?.let {
                            textView.text = "Today: ${it.WeatherText}, ${it.Temperature.Metric.Value} ${it.Temperature.Metric.Unit}"
                        } ?: run {
                            textView.text = "No weather data available"
                        }
                    } else {
                        textView.text = "Error: ${response.code()}"
                    }
                }

                override fun onFailure(call: Call<List<WeatherResponse>>, t: Throwable) {
                    textView.text = "Failed: ${t.message}"
                }
            })

        return root
    }

    companion object {
        @JvmStatic
        fun newInstance(param1: String, param2: String) =
            TodayFragment().apply {
                arguments = Bundle().apply {
                    putString(ARG_PARAM1, param1)
                    putString(ARG_PARAM2, param2)
                }
            }

        private const val ARG_PARAM1 = "param1"
        private const val ARG_PARAM2 = "param2"
    }
}
