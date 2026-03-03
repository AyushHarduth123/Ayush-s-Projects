package com.example.tabbedactivity

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment

class TabFragment : Fragment() {

    companion object {
        private const val ARG_TEXT = "arg_text"

        fun newInstance(text: String): TabFragment {
            val fragment = TabFragment()
            val bundle = Bundle()
            bundle.putString(ARG_TEXT, text)
            fragment.arguments = bundle
            return fragment
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        val view = inflater.inflate(R.layout.fragment_tab, container, false)
        val textView: TextView = view.findViewById(R.id.textView)
        textView.text = arguments?.getString(ARG_TEXT)
        return view
    }
}
