package com.example.tabbedactivity

import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentActivity
import androidx.viewpager2.adapter.FragmentStateAdapter

class TabPagerAdapter(activity: FragmentActivity) : FragmentStateAdapter(activity) {
    override fun getItemCount(): Int = 3

    override fun createFragment(position: Int): Fragment {
        return when (position) {
            0 -> TabFragment.newInstance("Welcome to Home Tab")
            1 -> TabFragment.newInstance("This is your Profile Tab")
            2 -> TabFragment.newInstance("Settings content here")
            else -> TabFragment.newInstance("Unknown")
        }
    }
}
