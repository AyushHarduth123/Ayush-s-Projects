package com.example.weathertabbedapp

import androidx.fragment.app.Fragment

class SectionPagerAdapter {
    fun getItem(position: Int): Fragment {
        return when (position) {
            0 -> TodayFragment()
            1 -> FiveDayFragment()
            2 -> CityWeatherFragment()
            else -> TodayFragment()
        }
    }

    fun getPageTitle(position: Int): CharSequence {
        return when (position) {
            0 -> "TODAY"
            1 -> "5-DAY FORECAST"
            2 -> "CITY WEATHER"
            else -> ""
        }
    }

}