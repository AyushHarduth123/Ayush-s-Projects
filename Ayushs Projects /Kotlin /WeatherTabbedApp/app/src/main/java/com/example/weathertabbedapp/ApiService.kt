package com.example.weathertabbedapp

import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Path
import retrofit2.http.Query

interface ApiService {

    @GET("currentconditions/v1/{locationKey}")
    fun getTodayWeather(
        @Path("locationKey") locationKey: String,
        @Query("apikey") apiKey: String
    ): Call<List<WeatherResponse>>

    @GET("forecasts/v1/daily/5day/{locationKey}")
    fun getFiveDayForecast(
        @Path("locationKey") locationKey: String,
        @Query("apikey") apiKey: String
    ): Call<ForecastResponse>

    @GET("locations/v1/cities/search")
    fun getLocationKey(
        @Query("q") cityName: String,
        @Query("apikey") apiKey: String
    ): Call<List<LocationResponse>>
}
