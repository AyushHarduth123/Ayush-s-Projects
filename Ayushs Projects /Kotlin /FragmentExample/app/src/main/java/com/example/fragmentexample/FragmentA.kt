package com.example.fragmentexample

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.fragment.app.Fragment

class FragmentA : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_a, container, false)

        val button = view.findViewById<Button>(R.id.btnGoToB)
        button.setOnClickListener {
            // Replace FragmentA with FragmentB
            parentFragmentManager.beginTransaction()
                .replace(R.id.fragment_container, FragmentB())
                .addToBackStack(null) // Allow back navigation
                .commit()
        }

        return view
    }
}
