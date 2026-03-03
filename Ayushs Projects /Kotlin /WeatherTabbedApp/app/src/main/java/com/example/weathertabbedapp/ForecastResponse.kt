package com.example.weathertabbedapp


data class ForecastResponse(
    val DailyForecasts: List<DailyForecast>
)

data class DailyForecast(
    val Date: String,
    val Temperature: TempRange
)

data class TempRange(
    val Minimum: UnitData,
    val Maximum: UnitData
)
