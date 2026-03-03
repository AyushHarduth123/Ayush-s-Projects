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

class FiveDayFragment : Fragment() {

    private lateinit var textView: TextView
    private val apiKey = "YOUR_ACCUWEATHER_API_KEY"
    private val locationKey = "YOUR_LOCATION_KEY" // e.g., "328328" for Johannesburg

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        arguments?.let {
            param1 = it.getString(ARG_PARAM1)
            param2 = it.getString(ARG_PARAM2)
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        val root = inflater.inflate(R.layout.fragment_five_day, container, false)
        textView = root.findViewById(R.id.fiveDayText)

        RetrofitClient.instance.getFiveDayForecast(locationKey, apiKey)
            .enqueue(object : Callback<ForecastResponse> {
                override fun onResponse(
                    call: Call<ForecastResponse>,
                    response: Response<ForecastResponse>
                ) {
                    if (response.isSuccessful) {
                        val forecasts = response.body()?.DailyForecasts
                        val display = forecasts?.joinToString("\n") {
                            "${it.Date.take(10)}: Min ${it.Temperature.Minimum.Value}° / Max ${it.Temperature.Maximum.Value}°"
                        } ?: "No forecast data available"
                        textView.text = display
                    } else {
                        textView.text = "API Error: ${response.code()}"
                    }
                }

                override fun onFailure(call: Call<ForecastResponse>, t: Throwable) {
                    textView.text = "Error: ${t.message}"
                }
            })

        return root
    }

    private var param1: String? = null
    private var param2: String? = null

    companion object {
        private const val ARG_PARAM1 = "param1"
        private const val ARG_PARAM2 = "param2"

        @JvmStatic
        fun newInstance(param1: String, param2: String) =
            FiveDayFragment().apply {
                arguments = Bundle().apply {
                    putString(ARG_PARAM1, param1)
                    putString(ARG_PARAM2, param2)
                }
            }
    }
}
