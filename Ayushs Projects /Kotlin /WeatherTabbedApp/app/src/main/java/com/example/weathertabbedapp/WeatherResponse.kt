package com.example.weathertabbedapp

data class WeatherResponse(
    val WeatherText: String,
    val Temperature: Temperature
)

data class Temperature(
    val Metric: UnitData
)

data class UnitData(
    val Value: Float,
    val Unit: String
)
